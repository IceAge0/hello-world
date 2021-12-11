
import requests
from lxml import etree
import os
 
#必应图片网页地址 https://bing.ioliu.cn/?p=3
url = 'https://bing.ioliu.cn/'
#浏览器参数
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    #referer的作用就是记录你在访问一个目标网站时，在访问前你的原网站的地址
	'Referer':'http://bing.ioliu.cn'
}
#图片的张数
number = 0

 #下载网页
html = requests.get(url,headers=header).text 
   
#构造xpath的解析对象
etree_html = etree.HTML(html)      
             
#获取图片地址
# // | 文档的任意位置 
# @属性名 | 选取属性名所对应的方法 
img_url = etree_html.xpath('//img/@src')
     
#判断是否存在文件夹picture，不存在则创建一个
if not os.path.exists('picture'):
	os.mkdir('picture')   


#下载图片并保存至指定位置
for img_list in img_url:  
	#replace()方法：str.replace(old, new[, max])
	#参数
	#old -- 将被替换的子字符串。
	#new -- 新字符串，用于替换old子字符串。
	#max -- 可选字符串, 替换不超过 max 次
	#替换图片清晰度
    img_list = img_list.replace('640x480','1920x1080')
    #print(img_list)
	#获取图片内容
    img = requests.get(img_list,headers=header).content
    number+=1
    print('正在下载第{}张图片'.format(number))
	
    img_name = 'picture\\{}.jpg'.format(number)
    with open(img_name,'wb') as save_img:
		#写入图片数据
        save_img.write(img)
