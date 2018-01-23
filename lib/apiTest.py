# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2018/1/22 09:35'

import os
import json
import urllib
#import urllib.request as urllib2
import time


from baiduapi import serviceSetup,access_token
#from demoDir import dirOcrTreatment



client = serviceSetup()
filePath = "/Users/MRJ/PycharmProjects/OCR v1.0/OCR_pic/fapiao_pic.png"
options = {}
options["result_type"] = "json"

"""TODO:等次数恢复后再调试"""
""" 调用表格识别结果 """

# result = client.tableRecognitionAsync(filePath, options)
# result_key_list = result.get("result")
# print (result_key_list)
# result_id = result_key_list[0].get("request_id")

# result_content = client.getTableRecognitionResult(result_id)
# #print("result_content：")
# #print (result_content)
#
# result_json = (json.dumps(result_content, indent=4, sort_keys=True))
# print ("result_json："+result_json)
# result_dict = json.loads(result_json)
# #result_dict1 = result_dict.get("result").get("ret_msg").encode("utf-8")
# print (result_dict)
#
# while True:
#     time.sleep(2)
#     result_content = client.getTableRecognitionResult(result_id)
#     #print("result_content：")
#     #print (result_content)
#
#     result_json = (json.dumps(result_content, indent=4, sort_keys=True))
#     print ("result_json：" + result_json)
#     #result_dict = json.loads(result_json)
#     #result_dict1 = result_dict.get("result").get("ret_msg").encode("utf-8")
#     #print (result_dict)



'''

url = "https://aip.baidubce.com/rest/2.0/solution/v1/iocr/recognise?access_token=" + access_token()
params = {"request_id":result_id, "result_type":'json'}
params = urllib.urlencode(params)
request = urllib2.Request(url,params)
request.add_header('Content-Type', 'application/x-www-form-urlencoded')

while True:
    time.sleep(2)
    response = urllib2.urlopen(request)
    content = response.read()
    print content
'''
"""自定义模板接口调用"""

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

url = "https://aip.baidubce.com/rest/2.0/solution/v1/iocr/recognise"
image = get_file_content('/Users/MRJ/PycharmProjects/OCR v1.0/OCR_pic/发票扫描/扫描0001.jpg')
#templateSign = "6bbaaf76e8824898b3bf473aeec777b9"

#content = urllib2.Request(url,templateSign,image)
#content = client.custom(image,templateSign)

#print content
""" 读取图片 """


#image = get_file_content('example.jpg')
templateSign = "6bbaaf76e8824898b3bf473aeec777b9"

""" 调用自定义模版文字识别 """
print(client.custom(image, templateSign))



#增值税发票识别

# image = get_file_content(filePath)
# templateSign = "Nsdax2424asaAS791823112"
#
# client.custom(image, templateSign);
