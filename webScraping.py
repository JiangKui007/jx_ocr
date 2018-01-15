# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2018/1/15 10:59'

import urllib2

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

def main():
    url = "https://inv-veri.chinatax.gov.cn/"
    print download(url)

main()
#httpGet.abort()