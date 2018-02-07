# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2018/1/19 15:01'

import os
import time
from resize import resize
import ocrOutput as output
from zengzhishuiTemplate import zengzhishuiTemplate


def dirOcrTreatment():
    path = "/Users/MRJ/PycharmProjects/OCR v1.0/OCR_pic/发票扫描/" #文件夹目录
    files= os.listdir(path) #得到文件夹下的所有文件名称
    for file in files: #遍历文件夹
         ext = ("jpg","jpeg","png")
         if file.endswith(ext): #判断是否是文件夹，不是文件夹才打开
             wholePath = path+"/"+ file
             #输出OCR识别时的路径
             print ("~~~~~~~~~~~~~~~~~~~~~~~~~~")
             print ("OCR正在识别文件   "+file + "   请等待......")
             print ("~~~~~~~~~~~~~~~~~~~~~~~~~~")
             ajson = output.basicReadText(wholePath)
             output.generalOutput(ajson)


#定义一个二维数组
def getMatrix(rows,cols):
    matrix = [[0 for col in range(cols)] for row in range(rows)]
    return matrix
    # for i in range(rows):
    #     #for j in range(cols):
    #         print (matrix[i])
    #         #print (matrix[i][j])
    # print ('\n')
#getMatrix(8,8)

'''增值税发票核心处理单元'''
def zengzhishuifapiao_unit(file,path,txtf,):
    # 计数及时间计算
    unit_start_time = time.time()
    wholePath = path+"/"+ file
    #调用百度模板识别
    #TODO:上传图片前用opencv对图片进行处理，去掉图片中的红色
    content = zengzhishuiTemplate(wholePath)
    api_time = time.time()
    api_cost_time = api_time-unit_start_time
    print ("调用接口使用时间"+str(api_cost_time)+"s")
    #初始化错误代码
    isStructured = content.get("data").get("isStructured")
    error_code = content.get("error_code")
    error_msg = content.get("error_msg")
    #初始化列表及列表计数
    double_array = []
    list1 = []
    sep = ','
    content_data = content.get("data").get("ret")
    if error_code == 0 and isStructured == True:
        for k in content_data:
            #对从百度获取的data遍历
            word_name = k.get("word_name")
            word = k.get("word")
            #开票内容判别与数组显示
            if "开票内容#1#" in word_name:
                list1.append(word)
                if len(list1) == 8:
                    double_array.append(list1)
                    list1 = []
            elif "开票内容#2#" in word_name:
                list1.append(word)
                if len(list1) == 8:
                    double_array.append(list1)
                    list1 = []
            elif "开票内容#3#" in word_name:
                list1.append(word)
                if len(list1) == 8:
                    double_array.append(list1)
                    list1 = []
            elif "开票内容#4#" in word_name:
                list1.append(word)
                if len(list1) == 8:
                    double_array.append(list1)
                    list1 = []
            elif "开票内容#5#" in word_name:
                list1.append(word)
                if len(list1) == 8:
                    double_array.append(list1)
                    list1 = []
            elif "开票内容#6#" in word_name:
                list1.append(word)
                if len(list1) == 8:
                    double_array.append(list1)
                    list1 = []
            elif "开票内容#7#" in word_name:
                list1.append(word)
                if len(list1) == 8:
                    double_array.append(list1)
                    list1 = []
            elif "开票内容#8#" in word_name:
                list1.append(word)
                if len(list1) == 8:
                    double_array.append(list1)
                    list1 = []
            else:
                #主内容输出
                lines = word_name + ":" + word
                print (lines)
                txtf.write(lines+"\n")

        print ("开票内容存在"+str(len(double_array))+"条")
        for i in range(len(double_array)):
            #输出表格内容
            print (double_array[i])
            txtf.write(sep.join(double_array[i])+"\n")
        unit_end_time = time.time()
        cost_time = (unit_end_time-unit_start_time)
        print ("本地耗时"+str(cost_time-api_cost_time)+"s")
        print ("单元耗时"+str(cost_time)+"s")
        print (" ------------------------------")
        error_msg_local =  0
        return error_msg_local
    else:
        #扫描失败报错信息
        if isStructured == False:
            error_msg_local =  1
            #print ("扫描失败，请检查图片格式是否正确")
            #print (" ------------------------------")

        else:
            error_msg_local =  2
            #print ( "扫描失败，错误信息：" + error_msg)
            #print (" ------------------------------")
        return error_msg_local

'''增值税发票本地文件夹处理函数'''
def zengzhishuifapiao(path):
    #发票扫描路径导入
    files= os.listdir(path) #得到文件夹下的所有文件名称
    #计数及时间计算
    start_time = time.time()
    times = 0
    right_times = 0
    error_times = 0
    localTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    txtf = open("result"+localTime+".txt", 'a')
    print (" ------------------------------\n|正在对文件夹中的图片进行扫描......|\n ------------------------------")
    ext = ("jpg", "jpeg", "png")
    for file in files: #遍历文件夹
        if file.endswith(ext):  # 判断是否是文件夹，不是文件夹才打开
            times = times + 1
            #print ("|正在扫描第"+str(times)+"张:"+file+"\n ------------------------------")
            txtf.write("\n第"+str(times)+"张:"+file+"内容\n")
            #TODO:判断图片大小
            #file = resize(path +"/"+ file)
            report_msg = zengzhishuifapiao_unit(file,path,txtf,)  #调用增值税核心处理单元
            if report_msg == 0:
                right_times = right_times + 1
            else:
                error_times = error_times + 1
    end_time = time.time()
    cost_time = (end_time - start_time)
    #print ("处理全部文件共耗时" + str(cost_time) + "s,平均耗时"+str(cost_time/times))
    txtf.close()
    return times,right_times,error_times

if __name__ == "__main__":
    times,right_times,error_times =zengzhishuifapiao()
    print ("扫描结束，共识别"+str(times)+"次,正确识别次数"+str(right_times)+"条,错误识别次数"+str(error_times))