# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2018/1/9 09:52'

import tesserocr
import cv2

image = cv2.imread('/Users/MRJ/PycharmProjects/OCR v1.0/OCR_pic/timg.jpeg')

#算数平均法灰度处理
im_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
im_at_mean = cv2.adaptiveThreshold(im_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 10)

#高斯平滑
result = cv2.GaussianBlur(im_at_mean, (5, 5),1.5)
cv2.imwrite("fapiao_pic.png",im_at_mean)

api = tesserocr.PyTessBaseAPI(lang='chi_sim')


api.SetImageFile("fapiao_pic.png")
print api.GetUTF8Text().strip()