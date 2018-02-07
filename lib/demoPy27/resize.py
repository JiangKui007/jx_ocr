# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2018/1/26 16:27'
import os
from PIL import Image


def resize(filename):
    im= Image.open(filename)
    w,h = im.size
    if w or h > 1024 :
        if w > h:
            times = w/1024
            im= im.resize (1024,h//times)
            return im
        else:
            times = h/1024
            im= im.resize ((w//times,1024) , Image.ANTIALIAS)
        im.save(filename, 'jpeg')
        return filename
#im = resize("/Users/MRJ/PycharmProjects/OCR v1.0/OCR_pic/20180126/扫描0007.jpg")
#print im.size
if __name__ == "__main__":
    path = "/Users/MRJ/PycharmProjects/OCR v1.0/OCR_pic/20180126"
    files = os.listdir(path)  # 得到文件夹下的所有文件名称
    for file in files:
        resize(path+"/"+file)
