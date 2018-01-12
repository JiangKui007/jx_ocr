# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2018/1/9 08:51'

import sys
import cv2
import numpy as np

'''
主函数
'''
# #主函数
# if __name__ == '__main__':
#     if len(sys.argv)>1:
#         image = cv2.imread(sys.argv[1],cv2.IMREAD_COLOR)
#     else:
#         print "Usge:Python HLS.py imageFile"

#显示原图
image = cv2.imread("/Users/MRJ/PycharmProjects/OCR v1.0/OCR_pic/Snip20180112_2.png")
"""
三原色分色
"""
b,g,r = cv2.split(image)
# cv2.imwrite(b,"blue.jpg")
# cv2.imwrite(g,'Green.jpg')
# cv2.imwrite(r,'Red.jpg')
cv2.imshow("image",image)
cv2.imshow("Blue 1",b)

cv2.imshow("Green 1",g)
cv2.imshow("Red 1",r)

print("票据读取成功")

cv2.waitKey(0)
cv2.destroyAllWindows()

#fImg = image.astype(np.float32)




#vector<Mat> channels

