# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2018/1/4 10:22'

#filePath = input("")
#print ("请输入文件路径\n")

'''from tesserocr import PyTessBaseAPI

images = ['sample.jpg', 'sample2.jpeg', 'sample3.jpg']

with PyTessBaseAPI() as api:
    for img in images:
        api.SetImageFile(img)
        print api.GetUTF8Text()
        print api.AllWordConfidences()'''

import tesserocr
from PIL import Image

print tesserocr.tesseract_version()  # print tesseract-ocr version
print tesserocr.get_languages()  # prints tessdata path and list of available languages

lang = "chi_sim"

image = Image.open('dingefapiao.jpg').convert('L')
image.save('aaa.tiff')

print tesserocr.image_to_text(image)  # print ocr text from image
# or
print tesserocr.file_to_text('aaa.tiff')