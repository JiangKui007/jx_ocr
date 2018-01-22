# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2018/1/8 11:25'

#import cv2

#img = cv2.imread("/Users/MRJ/PycharmProjects/OCR v1.0/fapiao1.jpg")
#GrayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Image", img)
#cv2.imshow("grayImage", GrayImage)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
"""
使用canny法对阈值处理
"""
import cv2 as cv
import numpy as np
image = cv.imread('/Users/MRJ/PycharmProjects/OCR v1.0/fapiao1.jpg')
# cv.imwrite("grayimg.jpg",cv.Canny(image,200,300))
# cv.imshow('srcImage', image)
# cv.imshow('grayImage', cv.imread("grayimg.jpg"))
# cv.waitKey(0)
# cv.destroyAllWindows()


"""
算数平均法对阈值处理
"""
# im_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# im_at_mean = cv.adaptiveThreshold(im_gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 5, 10)
# cv.imwrite("grayimg1.jpg",im_at_mean)
# cv.imshow('srcImage', image)
# cv.imshow('grayImage', cv.imread("grayimg1.jpg"))
# cv.waitKey(0)
# cv.destroyAllWindows()


"""
高斯加权平均法对阈值处理
"""
im_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
im_at_mean = cv.adaptiveThreshold(im_gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 5, 7)
cv.imwrite("grayimg2.jpg",im_at_mean)
cv.imshow('srcImage', image)
cv.imshow('grayImage', cv.imread("grayimg2.jpg"))
cv.waitKey(0)
cv.destroyAllWindows()





# import cv2
# import numpy as np
# from matplotlib import pyplot as plt
#
# image = cv2.imread("/Users/MRJ/PycharmProjects/OCR v1.0/fapiao1.jpg")
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# plt.subplot(131), plt.imshow(image, "gray")
# plt.title("source image"), plt.xticks([]), plt.yticks([])
# plt.subplot(132), plt.hist(image.ravel(), 256)
# plt.title("Histogram"), plt.xticks([]), plt.yticks([])
# ret1, th1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)  #方法选择为THRESH_OTSU
# plt.subplot(133), plt.imshow(th1, "gray")
# plt.title("OTSU,threshold is " + str(ret1)), plt.xticks([]), plt.yticks([])
# plt.show()