# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2018/1/23 09:46'
import json
from baiduapi import serviceSetup

client = serviceSetup()

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


""" 调用自定义模版文字识别 """
def zengzhishuiTemplate(filePath):
    #图片路径和模板id
    image = get_file_content(filePath)
    templateSign = "6bbaaf76e8824898b3bf473aeec777b9"

    ticket_content = client.custom(image, templateSign)
    return ticket_content
# content = zengzhishuiTemplate("/Users/MRJ/PycharmProjects/OCR v1.0/OCR_pic/发票扫描/扫描.jpg")
#
# content_data = content.get("data").get("ret")
# for k in content_data:
#     print (k.get("word_name"))
#     print (k.get("word"))

