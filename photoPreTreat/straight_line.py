# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2018/1/8 17:04'

# coding=utf-8
"""
直线消除处理
TODO：直线参数仍需探索
"""


import cv2
import numpy as np

img = cv2.imread("grayimg1.jpg")

img = cv2.GaussianBlur(img, (3, 3), 0)
edges = cv2.Canny(img, 50, 150, apertureSize=3)
lines = cv2.HoughLines(edges, 0.5, np.pi / 180, 118)
result = img.copy()
cv2.imwrite("straight_line1.jpg",result)
# 经验参数
minLineLength = 200
maxLineGap = 15
lines = cv2.HoughLinesP(edges, 0.5, np.pi / 180, 80, minLineLength, maxLineGap)
for x1, y1, x2, y2 in lines[0]:
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow("Origin", img)
cv2.imshow('Result', cv2.imread("straight_line1.jpg"))

cv2.waitKey(0)
cv2.destroyAllWindows()