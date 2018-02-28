# jx_ocr
应用tensorflow实现票据识别

这款OCR仍然处于开发阶段。demo可以运行~/OCR v1.0/ocrFile/fileOcrTrement.py 将图片文件地址换成你想用的。

欢迎提交issues讨论。
# 项目小结
## 1.	项目目录概况：
-------
    图片目录：/OCR_pic
    图片处理目录：/ocrFile、/photoPretreatLib
    图片识别引擎主要处理程序目录：/lib
    其他插件及其文档地址：
        tesseract       https://github.com/tesseract-ocr/tesseract
        chinese-ocr     https://github.com/chineseocr/chinese-ocr
        Chinese-ocr-with-cpu  https://github.com/eragonruan/text-detection-ctpn
        Mnist-master    http://wiki.jikexueyuan.com/project/tensorflow-zh/tutorials/mnist_beginners.html
        Pyocr           https://github.com/openpaperwork/pyocr
        sceneReco       https://github.com/bear63/sceneReco
## 2. OCR识别
--------
	目录：/lib
	依赖安装：/lib/demoPy27/requirements.txt
	文件：
        baiduapi.py  文档地址：http://ai.baidu.com/docs#/ImageClassify-Python-SDK/top
        demoDir.py  批量ocr处理图片
        demoFile.py  逐个ocr处理图片
        ocrOutput.py  输出接口
        outputXml.py  NC凭证post上传接口
        resize.py  图片大小规范文件
        zengzhishuiTemplate.py  增值税发票模板接口
        /demoPy27  兼容python2的百度ocr处理文档
## 3.图片预处理与OCR识别测试脚本：
---------
    目录：/ocrFile
    依赖：opencv3、tesseract、tensorflow
    文件：
        electronic_tickets_ocr.py  电子发票预处理及tesseract识别
        mnist_advance.py  机器学习强化版脚本
        mnist_test.py  机器学习初步脚本
        tesseracocr.py  tesseract图片识别脚本
        ticketocr.py  百度aip票据识别脚本
## 4. 图片opencv处理：
---------
    目录：/photoPretreatLib
    文件：
        photoPretreatLib/color_split.py  opencv三原色分色算法
        photoPretreatLib/fileOcrTrement.py  opencv+tesseract处理算法脚本
        photoPretreatLib/opencv_test.py  opencv图像灰度处理算法
        photoPretreatLib/picTreatment.py  pil图片压缩脚本
        photoPretreatLib/pil_lib.py  pil图片处理函数
        photoPretreatLib/smoothing_method.py  opencv图片平滑处理算法
        photoPretreatLib/straight_line.py  opencv图片霍夫直线处理算法
        photoPretreatLib/threshold_method.py  opencv 图片二值化阈值处理算法
## 部分参考文献：
----------
    邬满. 基于跳变检测和Tesseract的机打发票识别算法[J]. 信息与电脑:理论版, 2015(18):43-45.
    王宸敏. 基于OCR技术的化验单识别方法研究[D]. 浙江大学, 2016.
    万松. 基于Tesseract-OCR的名片识别系统的研究与实现[D]. 华南理工大学, 2014.
    王希晨. 基于Tesseract的电子票据云平台的设计与实现[D]. 南京大学, 2016.
    张扬. 基于Tesseract光学字符辨识应用的设计与实现[D]. 西安电子科技大学, 2013.
    程育恒. 基于Tesseract开源OCR引擎的证件识别系统的设计与实现[D]. 东华大学, 2014.
    胡文, 马玲玉. 基于OpenCV手机拍照快递单文字识别的研究[J]. 哈尔滨商业大学学报(自然科学版), 2015(5):564-568.
