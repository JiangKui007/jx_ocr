# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2018/1/5 10:48'
"""

用PIL库对图片处理，获取图片位置信息

"""

from PIL import Image

one = Image.open(r'/Users/MRJ/PycharmProjects/OCR v1.0/temporary_file/a1.tiff')
picSize = one.size
picMode = one.mode
picFormat = one.format
print picSize, picMode, picFormat

def compress_image(img, w=1024, h=1024):
    '''
    过大图片压缩
    '''
    img.thumbnail((w,h))
    img.save('a7.png','PNG')
    print u'成功将图片压缩至1M以下'

if picSize[0] > 1024 or picSize[1] >1024 :
    one = compress_image(one,1024,1024)
    one.show()
def cut_image(img):
    '''
    截图, 旋转，再粘贴
    '''
    #eft, upper, right, lower
    #x y z w  x,y 是起点， z,w是偏移值
    width, height = img.size
    box = (width-200, height-100, width, height)
    region = img.crop(box)
    #旋转角度
    region = region.transpose(Image.ROTATE_180)
    img.paste(region, box)
    img.save('test2.jpg', 'JPEG')
    print u'重新拼图成功'