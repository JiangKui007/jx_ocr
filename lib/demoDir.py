# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2018/1/19 15:01'

import os
import ocrOutput as output

def dirOcrTreatment():
    path = "/Users/MRJ/PycharmProjects/OCR v1.0/OCR_pic/发票扫描" #文件夹目录
    files= os.listdir(path) #得到文件夹下的所有文件名称
    for file in files: #遍历文件夹
         ext = ("jpg","jpeg","png")
         if file.endswith(ext): #判断是否是文件夹，不是文件夹才打开
             wholePath = path+"/"+ file
             #输出OCR识别时的路径
             print "~~~~~~~~~~~~~~~~~~~~~~~~~~"
             print "OCR正在识别文件   "+file + "   请等待......"
             print "~~~~~~~~~~~~~~~~~~~~~~~~~~"
             ajson = output.basicReadText(wholePath)
             output.generalOutput(ajson)

dirOcrTreatment()
