# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2018/1/4 10:22'


'''from tesserocr import PyTessBaseAPI

images = ['sample.jpg', 'sample2.jpeg', 'sample3.jpg']

with PyTessBaseAPI() as api:
    for img in images:
        api.SetImageFile(img)
        print api.GetUTF8Text()
        print api.AllWordConfidences()'''
import os
import os.path

import tesserocr
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
import time

#print tesserocr.tesseract_version()  # print tesseract-ocr version
#print tesserocr.get_languages()  # prints tessdata path and list of available languages

#lang = "chi_sim"



'''获取图片路径和处理模式'''
#filePath = input("")
#print ("请输入文件路径\n")

imagePath = ('temporary_file/a2.tiff')
convertMode = ('L')


'''将图片转为灰度图'''
image = Image.open(imagePath).convert(convertMode)
image.save('temporary_file/a5.tiff')

'''用恒定的阈值设置转换表'''
#threshold 灰度系数
#table 二值化阈值数组

threshold  =   200
table  =  []
for  i  in  range(256):
      if  i  <  threshold:
         table.append(0)
      else :
         table.append(1)

#由表转换为二进制图像

'''二值法函数'''
def binarizing(im, threshold):
    pixdata = im.load()
    w, h = im.size
    for j in range(h):
        for i in range(w):
            if pixdata[i, j] < threshold:
                pixdata[i, j] = 0
            else:
                pixdata[i, j] = 255
    return im

'''图片去噪'''
def denoising(im):
    pixdata = im.load()
    w, h = im.size
    for j in range(1, h - 1):
        for i in range(1, w - 1):
            count = 0
            if pixdata[i, j - 1] > 245:
                count = count + 1
            if pixdata[i, j + 1] > 245:
                count = count + 1
            if pixdata[i + 1, j] > 245:
                count = count + 1
            if pixdata[i - 1, j] > 245:
                count = count + 1
            if count > 2:
                pixdata[i, j] = 255
    return im


bim = image.point(table,'1')

"""使用tesserocr图像识别引擎对图片识别"""
bim.save('temporary_file/a6.tiff')

#api法调用tesserocr
api = tesserocr.PyTessBaseAPI(lang='chi_sim')
api.SetImageFile('temporary_file/a6.tiff')
print api.GetUTF8Text().strip()
#print tesserocr.image_to_text(image)  # print ocr text from image
# or
#调用file_to_text方法
print tesserocr.file_to_text('temporary_file/a4.tiff',lang='chi_sim')