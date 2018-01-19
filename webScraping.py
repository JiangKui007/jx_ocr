# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2018/1/15 10:59'

import urllib2
import lxml.html
import os
import time
"""
爬取相关url网页全部内容
"""
def download(url,num_retries = 2):
    print 'Downloading:',url
    try:
        return urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, num_retries-1)
    return html

def parse_form(html):
    tree = lxml.html.formstring(html)
    data = {}
    for e in tree.cssselect('form input'):
        if e.get('name'):
            data[e.get('name')] = e.get('value')
    return data

"""
使用Selelnium伪装指定本地的50.0版本火狐浏览器
"""
import unittest
#from selelnium import webbrowser
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

dictInput = {}
class Test(unittest.TestCase):
    def setUp(self):
        self.firefoxdriver = "/Applications/Firefox.app" # 将chromedriver.exe拷贝到你想要调用的chrome安装路径下即可
        os.environ["webdriver.firefox.driver"] = self.firefoxdriver
        self.browser = webdriver.Firefox(self.firefoxdriver)
    def test(self):
        self.browser.get('https://inv-veri.chinatax.gov.cn/')#此处xxxx为网页的url
    #def sendText(self):
        self.browser.find_element_by_id('fpdm').send_keys('Selenium')
"""
主函数
"""
def main():
    url = "https://inv-veri.chinatax.gov.cn/"
    #url =
    print do8wnload(url)

main()
#httpGet.abort()