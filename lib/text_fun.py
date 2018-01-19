# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2018/1/12 14:23'

import sys

filePath = '/Users/MRJ/PycharmProjects/OCR v1.0/OCR_pic/通用机打发票.jpg'
def get_file_content(filePath):
    with open(filePath,'rb') as fp:
        return fp.read()
