# -*- encoding=utf-8 -*-  
''''' 
author: orangleliu 
pil处理图片，验证，处理 
大小，格式 过滤 
压缩，截图，转换 
 
图片库最好用Pillow 
还有一个测试图片test.jpg, 一个log图片，一个字体文件 
'''  
  
#图片的基本参数获取  
try:  
    from PIL import Image, ImageDraw, ImageFont, ImageEnhance  
except ImportError:  
    import Image, ImageDraw, ImageFont, ImageEnhance  
  
def compress_image(img, w=128, h=128):  
    ''''' 
    缩略图 
    '''  
    img.thumbnail((w,h))  
    im.save('test1.png', 'PNG')  
    print u'成功保存为png格式, 压缩为128*128格式图片'  
  
def cut_image(img):  
    ''''' 
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
  
def logo_watermark(img, logo_path):  
    ''''' 
    添加一个图片水印,原理就是合并图层，用png比较好 
    '''  
    baseim = img  
    logoim = Image.open(logo_path)  
    bw, bh = baseim.size  
    lw, lh = logoim.size  
    baseim.paste(logoim, (bw-lw, bh-lh))  
    baseim.save('test3.jpg', 'JPEG')  
    print u'logo水印组合成功'  
  
def text_watermark(img, text, out_file="test4.jpg", angle=23, opacity=0.50):  
    ''''' 
    添加一个文字水印，做成透明水印的模样，应该是png图层合并 
    http://www.pythoncentral.io/watermark-images-python-2x/ 
    这里会产生著名的 ImportError("The _imagingft C module is not installed") 错误 
    Pillow通过安装来解决 pip install Pillow 
    '''  
    watermark = Image.new('RGBA', img.size, (255,255,255)) #我这里有一层白色的膜，去掉(255,255,255) 这个参数就好了  
  
    FONT = "msyh.ttf"  
    size = 2  
  
    n_font = ImageFont.truetype(FONT, size)                                       #得到字体  
    n_width, n_height = n_font.getsize(text)  
    text_box = min(watermark.size[0], watermark.size[1])  
    while (n_width+n_height <  text_box):  
        size += 2  
        n_font = ImageFont.truetype(FONT, size=size)  
        n_width, n_height = n_font.getsize(text)                                   #文字逐渐放大，但是要小于图片的宽高最小值  
  
    text_width = (watermark.size[0] - n_width) / 2  
    text_height = (watermark.size[1] - n_height) / 2  
    #watermark = watermark.resize((text_width,text_height), Image.ANTIALIAS)  
    draw = ImageDraw.Draw(watermark, 'RGBA')                                       #在水印层加画笔  
    draw.text((text_width,text_height),  
              text, font=n_font, fill="#21ACDA")  
    watermark = watermark.rotate(angle, Image.BICUBIC)  
    alpha = watermark.split()[3]  
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)  
    watermark.putalpha(alpha)  
    Image.composite(watermark, img, watermark).save(out_file, 'JPEG')  
    print u"文字水印成功"  
  
  
#等比例压缩图片  
def resizeImg(img, dst_w=0, dst_h=0, qua=85):  
    ''''' 
    只给了宽或者高，或者两个都给了，然后取比例合适的 
    如果图片比给要压缩的尺寸都要小，就不压缩了 
    '''  
    ori_w, ori_h = im.size  
    widthRatio = heightRatio = None  
    ratio = 1  
  
    if (ori_w and ori_w > dst_w) or (ori_h and ori_h  > dst_h):  
        if dst_w and ori_w > dst_w:  
            widthRatio = float(dst_w) / ori_w                                      #正确获取小数的方式  
        if dst_h and ori_h > dst_h:  
            heightRatio = float(dst_h) / ori_h  
  
        if widthRatio and heightRatio:  
            if widthRatio < heightRatio:  
                ratio = widthRatio  
            else:  
                ratio = heightRatio  
  
        if widthRatio and not heightRatio:  
            ratio = widthRatio  
  
        if heightRatio and not widthRatio:  
            ratio = heightRatio  
  
        newWidth = int(ori_w * ratio)  
        newHeight = int(ori_h * ratio)  
    else:  
        newWidth = ori_w  
        newHeight = ori_h  
  
    im.resize((newWidth,newHeight),Image.ANTIALIAS).save("test5.jpg", "JPEG", quality=qua)  
    print u'等比压缩完成'  
  
    ''''' 
    Image.ANTIALIAS还有如下值： 
    NEAREST: use nearest neighbour 
    BILINEAR: linear interpolation in a 2x2 environment 
    BICUBIC:cubic spline interpolation in a 4x4 environment 
    ANTIALIAS:best down-sizing filter 
    '''  
  
#裁剪压缩图片  
def clipResizeImg(im, dst_w, dst_h, qua=95):  
    ''''' 
        先按照一个比例对图片剪裁，然后在压缩到指定尺寸 
        一个图片 16:5 ，压缩为 2:1 并且宽为200，就要先把图片裁剪成 10:5,然后在等比压缩 
    '''  
    ori_w,ori_h = im.size  
  
    dst_scale = float(dst_w) / dst_h  #目标高宽比  
    ori_scale = float(ori_w) / ori_h #原高宽比  
  
    if ori_scale <= dst_scale:  
        #过高  
        width = ori_w  
        height = int(width/dst_scale)  
  
        x = 0  
        y = (ori_h - height) / 2  
  
    else:  
        #过宽  
        height = ori_h  
        width = int(height*dst_scale)  
  
        x = (ori_w - width) / 2  
        y = 0  
  
    #裁剪  
    box = (x,y,width+x,height+y)  
    #这里的参数可以这么认为：从某图的(x,y)坐标开始截，截到(width+x,height+y)坐标  
    #所包围的图像，crop方法与php中的imagecopy方法大为不一样  
    newIm = im.crop(box)  
    im = None  
  
    #压缩  
    ratio = float(dst_w) / width  
    newWidth = int(width * ratio)  
    newHeight = int(height * ratio)  
    newIm.resize((newWidth,newHeight),Image.ANTIALIAS).save("test6.jpg", "JPEG",quality=95)  
    print  "old size  %s  %s"%(ori_w, ori_h)  
    print  "new size %s %s"%(newWidth, newHeight)  
    print u"剪裁后等比压缩完成"  
  
  
if __name__ == "__main__":  
    ''''' 
    主要是实现功能， 代码没怎么整理 
    '''  
    im = Image.open('test.jpg')  #image 对象  
    compress_image(im)  
  
    im = Image.open('test.jpg')  #image 对象  
    cut_image(im)  
  
    im = Image.open('test.jpg')  #image 对象  
    logo_watermark(im, 'logo.png')  
  
    im = Image.open('test.jpg')  #image 对象  
    text_watermark(im, 'Orangleliu')  
  
    im = Image.open('test.jpg')  #image 对象  
    resizeImg(im, dst_w=100, qua=85)  
  
    im = Image.open('test.jpg')  #image 对象  
    clipResizeImg(im, 100, 200)  