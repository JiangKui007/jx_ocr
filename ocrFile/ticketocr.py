# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2018/1/3 13:37'

"""

百度aip票据识别脚本

"""

from aip import AipOcr
import json

#定义常量
APP_ID = '10618664'
API_KEY = 's37kdgQPRKnSFmdjgwFnTXrl'
SECRET_KEY = 'cV9SvMl0gaVjGxTik7qH28kBb36bkS8G'

#初始化对象
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('/Users/MRJ/PycharmProjects/OCR v1.0/OCR_pic/WechatIMG1521514955423_.pic.jpg')
client.receipt(image);

""" 如果有可选参数 """
options = {}
options["recognize_granularity"] = "big"
options["probability"] = "true"
options["accuracy"] = "normal"
options["detect_direction"] = "true"

""" 带参数调用通用票据识别 """
result = client.receipt(image, options)

print (json.dumps(result)).decode("unicode-escape")
