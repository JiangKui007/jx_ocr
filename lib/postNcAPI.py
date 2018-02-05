# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2018/1/30 15:55'

import urllib

#import urllib.Request

import json
import urllib2
import tarfile

import urllib,urllib2

def doPost(data1,data2):
    data = urllib.urlencode({'data1':data1,'data2':data2})
    request = urllib2.Request("http://192.168.1.234:8090/service/XChangeServlet?account=001&receiver=040103",data)
    response = urllib2.urlopen(request)
    file = response.read()
    if response.code != 200:
        return ('error code:'+response.code)
    else:
        return file
if __name__ == "__main__":
    doPost("1","test")
