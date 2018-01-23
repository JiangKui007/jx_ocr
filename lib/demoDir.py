# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2018/1/19 15:01'

import os
import ocrOutput as output
from zengzhishuiTemplate import zengzhishuiTemplate


def dirOcrTreatment():
    path = "/Users/MRJ/PycharmProjects/OCR v1.0/OCR_pic/发票扫描" #文件夹目录
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


def zengzhishuifapiao():
    #发票扫描、普通发票扫描20张
    path = "/Users/MRJ/PycharmProjects/OCR v1.0/OCR_pic/普通发票扫描20张" #文件夹目录
    files= os.listdir(path) #得到文件夹下的所有文件名称
    times = 1
    print (" ------------------------------\n|正在对文件夹中的图片进行扫描......|\n ------------------------------")
    for file in files: #遍历文件夹
         ext = ("jpg","jpeg","png")
         if file.endswith(ext): #判断是否是文件夹，不是文件夹才打开
            wholePath = path+"/"+ file
            print ("|正在扫描第"+str(times)+"张:"+file+"\n ------------------------------")
            #调用百度模板识别
            #TODO:上传图片前用opencv对图片进行处理，去掉图片中的红色
            content = zengzhishuiTemplate(wholePath)
            #初始化错误代码
            isStructured = content.get("data").get("isStructured")
            error_code = content.get("error_code")
            error_msg = content.get("error_msg")
            #初始化列表及列表计数
            list1 = []
            list2 = []
            list3 = []
            list4 = []
            list5 = []
            list6 = []
            list7 = []
            list8 = []
            list_num = 0
            #print (content)
            content_data = content.get("data").get("ret")
            #print (content_data)
            if error_code == 0 and isStructured == True:
                for k in content_data:
                    word_name = k.get("word_name")
                    word = k.get("word")
                    #TODO:待优化，二维数组
                    if "开票内容#1#" in word_name:
                        list1.append(word)
                        list_num = 1
                    elif "开票内容#2#" in word_name:
                        list2.append(word)
                        list_num = 2
                    elif "开票内容#3#" in word_name:
                        list3.append(word)
                        list_num = 3
                    elif "开票内容#4#" in word_name:
                        list4.append(word)
                        list_num = 4
                    elif "开票内容#5#" in word_name:
                        list5.append(word)
                        list_num = 5
                    elif "开票内容#6#" in word_name:
                        list6.append(word)
                        list_num = 6
                    elif "开票内容#7#" in word_name:
                        list7.append(word)
                        list_num = 7
                    elif "开票内容#8#" in word_name:
                        list8.append(word)
                        list_num = 8
                    else:
                        print (word_name + ":" + word)

                print ("开票内容存在"+str(list_num)+"条")
                print (list1)
                print (list2)
                print (list3)
                print (list4)
                print (list5)
                print (list6)
                print (list7)
                print (list8)
                print (" ------------------------------")
                times = times + 1
            else:
                if isStructured == False:
                    print ("扫描失败，请检查图片格式是否正确")
                    print (" ------------------------------")

                else:
                    print ( "扫描失败，错误信息：" + error_msg)
                    print (" ------------------------------")
                    #print (" ------------------------------")

                times = times + 1
zengzhishuifapiao()
print ("扫描结束")