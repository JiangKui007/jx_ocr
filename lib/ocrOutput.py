# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2018/1/19 15:52'

import baiduapi
import json
#import openPicFile
#读取图片
#filePath = '/Users/MRJ/PycharmProjects/OCR v1.0/OCR_pic/Snip20180113_6.png'

def get_file_content(filePath):
    with open(filePath,'rb') as fp:
        return fp.read()

    #定义参数变量
def serviceOptions():
    options = {
        'detect_direction': 'true',
        'language_type' : 'CHN_ENG',
    }
    return options
#options["detect_direction"] = "false"
#options["probability"] = "false"
    #调用通用文字识别接口
def basicOutputResult(client, filePath, options):
    result = client.basicGeneral(filePath, options)
    result_json = (json.dumps(result, indent=4, sort_keys=True))
    result_dict = json.loads(result_json)
    return result_dict
"""
机打发票检验及输出
"""
def jidafapiaoOutput(ajson):
    #判断机打发票内容
    for items in ajson:
        value = items.get("words")
        if "机打" in value:
            print (value)
            print ("\n 这是一张机打发票")
        if "发票代码" in value:
            #print ("发票代码为")
            print (value)
        if "网络发票号" in value:
            #print ("网络发票号为")
            print (value)
        if "付款方识别号" in value:
            print (value)
        if "收款方识别号" in value:
            print (value)
        if "收款单位" in value:
            print (value)
"""
通用输出
"""
def generalOutput(ajson):
    #尚未完成
    for items in ajson:
        print (items.get("words"))

"""
主程序
"""
def basicReadText(filename):
    client = baiduapi.serviceSetup()
    filePath = get_file_content(filename)
    options = serviceOptions()
    result_dict = basicOutputResult(client,filePath,options)
    ajson = result_dict.get("words_result")
    return ajson

if __name__ == "__main__":
    ajson = basicReadText ("/Users/MRJ/PycharmProjects/OCR v1.0/OCR_pic/其他图片/Snip20180112_2.png")
    generalOutput(ajson)