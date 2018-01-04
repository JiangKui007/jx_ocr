# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2018/1/3 15:58'

import os
import ctypes

lang = "chi_sim"
filename = "/Users/MRJ/PycharmProjects/OCR v1.0/OCR_pic/WechatIMG145.jpeg"
libname = "/usr/local/lib64/libtesseract.so.3"
TESSDATA_PREFIX = os.environ.get('TESSDATA_PREFIX')
if not TESSDATA_PREFIX:
    TESSDATA_PREFIX = "../"

tesseract = ctypes.cdll.LoadLibrary(libname)
tesseract.TessVersion.restype = ctypes.c_char_p
tesseract_version = tesseract.TessVersion()
api = tesseract.TessBaseAPICreate()
rc = tesseract.TessBaseAPIInit3(api, TESSDATA_PREFIX, lang)
if (rc):
    tesseract.TessBaseAPIDelete(api)
    print("Could not initialize tesseract.\n")
    exit(3)

text_out = tesseract.TessBaseAPIProcessPages(api, filename, None, 0)
result_text = ctypes.string_at(text_out)

print 'Tesseract-ocr version', tesseract_version
print result_text

