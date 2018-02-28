# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2018/2/7 10:21'


import os
import json
from zengzhishuiTemplate import zengzhishuiTemplate

def byteify(input):
    #解决python2编码问题
    if isinstance(input, dict):
        return {byteify(key): byteify(value) for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

'''增值税发票核心处理单元'''
def fileToDict(path):
    content = zengzhishuiTemplate(path)
    #print content
    dict1 = {}
    list1 = []
    isStructured = content.get("data").get("isStructured")
    error_code = content.get("error_code")
    error_msg = content.get("error_msg")
    content_data = content.get("data").get("ret")
    if  error_code==0 and isStructured == True:
        for words in content_data:
            words = byteify(words)
            word_name = words.get('word_name')
            word = words.get('word')
            #print word_name,word
            dict1[word_name] = word
            #print dict1
            #list1 = list1.append(dict1)
            #dict1 ={}
        return dict1
    else:
        return error_code,error_msg

def dirpath(path):
    #发票扫描路径导入
    files= os.listdir(path) #得到文件夹下的所有文件名称
    ext = ("jpg", "jpeg", "png")
    for file in files: #遍历文件夹
        if file.endswith(ext):  # 判断是否是文件夹，不是文件夹才打开
            ticket_data = fileToDict(path+file)
            if type(ticket_data) == 'dict':
                result = json.dumps(ticket_data, encoding='UTF-8', ensure_ascii=False)
                return result


if __name__  == "__main__":
    filepath = "/Users/MRJ/PycharmProjects/OCR v1.0/OCR_pic/普通发票扫描20张/1516691879890.jpg"
    dict1 = fileToDict(filepath)

    #调试：此处填图片文件夹
    # dir_path = "/Users/MRJ/PycharmProjects/OCR v1.0/OCR_pic/普通发票扫描20张/"
    # dir123 = fileToDict(dir_path)
    dict1 = json.dumps(dict1, encoding='UTF-8', ensure_ascii=False)

    print dict1
