# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2018/1/8 09:43'
"""
openCV 测试开发

"""

# 导入cv模块
import cv2
import numpy as np


def main():
    image = img
    maxValueGarylize(image)
    averageValueGary(image)
    weightedAverageValueGary(image)
"""
 最大值法图像灰度化
"""
def maxValueGarylize(image):
    grayimg = cv2.CreateImage(cv2.GetSize(image), image.depth, 1)
    for i in range(image.height):
        for j in range(image.width):
            grayimg[i, j] = max(image[i, j][0], image[i, j][1], image[i, j][2])
#    cv.ShowImage('srcImage', image)
    cv2.ShowImage('maxGrayImage', grayimg)
#    cv.WaitKey(0)

"""
平均值法图像灰度化
"""
def averageValueGary(image):
    grayimg = cv2.CreateImage(cv2.GetSize(image), image.depth, 1)
    for i in range(image.height):
        for j in range(image.width):
            grayimg[i, j] = (image[i, j][0] + image[i, j][1] + image[i, j][2]) / 3
#    cv2.ShowImage('srcImage', image)
    cv2.ShowImage('averageGrayImage', grayimg)
#    cv2.WaitKey(0)
"""
加权平均值法图像灰度化
"""
def weightedAverageValueGary(image):
    grayimg = cv2.CreateImage(cv2.GetSize(image), image.depth, 1)
    for i in range(image.height):
        for j in range(image.width):
            grayimg[i, j] = 0.3 * image[i, j][0] + 0.59 * image[i, j][1] + 0.11 * image[i, j][2]
#    cv2.ShowImage('srcImage', image)
    cv2.ShowImage('weightedGrayImage', grayimg)
#    cv2.WaitKey(0)



# 读取图像，支持 bmp、jpg、png、tiff 等常用格式
img = cv2.imread("fapiao2.jpg")
GrayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 创建窗口并显示图像
# cv.namedWindow("Image")
cv2.imshow("GrayImage", GrayImage)
cv2.imshow("Image", img)
# 释放窗口
#cv2.destroyAllWindows()
main()
cv2.waitKey(0)
cv2.destroyAllWindows()
