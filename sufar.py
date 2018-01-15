# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2018/1/15 14:01'


def foo(fun):
    def warp():
        print ("start")
        fun()
        print("end")
        print fun.__name__
    return warp


def bar():
    print("I am in Bar()")

f = foo(bar)
f()

@foo
def bur():
    print("I am in Bur()")

bur()