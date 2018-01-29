# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2018/1/12 14:23'

import sys
from baiduapi import serviceSetup
from ocrOutput import basicReadText

filePath = '/Users/MRJ/PycharmProjects/OCR v1.0/OCR_pic/20180126/扫描0008.jpg'
def get_file_content(filePath):
    with open(filePath,'rb') as fp:
        return fp.read()
content = get_file_content(filePath)
client = serviceSetup
ajson = basicReadText(filePath)
for items in ajson:
    print (items.get('words'))
#ajson_dict = ajson.loads(ajson)
#print (type(ajson_dict))
#print (ajson)
