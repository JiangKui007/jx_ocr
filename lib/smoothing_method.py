# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2018/1/8 16:44'

import cv2

img = cv2.imread("grayimg2.jpg")


"""
低通滤波平滑
"""
# result = cv2.boxFilter(img,-1, (5, 5))
# cv2.imwrite("smoothing.jpg",result)
#
# cv2.imshow("Origin", img)
# cv2.imshow("Blur", cv2.imread("smoothing.jpg"))
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

"""
高斯平滑
"""
# result = cv2.GaussianBlur(img, (5, 5),1.5)
# #元组为模糊范围，1.5为模糊度
# cv2.imwrite("smoothing1.jpg",result)
#
# cv2.imshow("Origin", img)
# cv2.imshow("Blur", cv2.imread("smoothing1.jpg"))
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

"""
中值滤波平滑
"""
result = cv2.medianBlur(img,3)
cv2.imwrite("smoothing2.jpg",result)

cv2.imshow("Origin", img)
cv2.imshow("Blur", cv2.imread("smoothing2.jpg"))

cv2.waitKey(0)
cv2.destroyAllWindows()
