
# coding=utf-8
import urllib as ulb
import numpy as np
import PIL.ImageFile as ImageFile
import cv2
import random
 
# 收集到的常用Header
my_headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
]
 
 
# 获取影像数据
def getImage(url):
    # 用urllib2库链接网络图像
    response = ulb.Request(url)
 
    # 随机选择一个Header伪装成浏览器
    response.add_header('User-Agent', random.choice(my_headers))
 
    # 打开网络图像文件句柄
    fp = ulb.urlopen(response)
 
    # 定义图像IO
    p = ImageFile.Parser()
 
    # 开始图像读取
    while 1:
        s = fp.read(1024)
        if not s:
            break
        p.feed(s)
 
    # 得到图像
    im = p.close()
 
    # 将图像转换成numpy矩阵
    arr = np.array(im)
 
    # 将图像RGB通道变成BGR通道，用于OpenCV显示
    pic = np.zeros(arr.shape, np.uint8)
    pic[:, :, 0] = arr[:, :, 2]
    pic[:, :, 1] = arr[:, :, 1]
    pic[:, :, 2] = arr[:, :, 0]
 
    return pic
 
 
img = getImage('http://static.fuwo.com/upload/attachment/1601/08/bea48ebeb5a811e58e9e00163e00254c.jpg')
cv2.imshow('image', img)
cv2.waitKey(0)
