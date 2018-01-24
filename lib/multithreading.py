# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2018/1/24 16:40'

#from demoDir import zengzhishuifapiao_unit

import threading
import time

def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print ("%s: %s") % (threadName, time.ctime(time.time()))
try:
    threading.thread.start_new_thread(print_time("Thread-1",2,) )
    threading.thread.start_new_thread(print_time("Thread-2", 4,) )
except:
    print ("Error:unable to start thread")