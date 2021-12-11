'''
写的正则是没问题的，但是解析到的url中只有一个符合要求
'''
import requests
import re
from bs4 import BeautifulSoup
url='https://wenku.baidu.com/view/4830a476534de518964bcf84b9d528ea80c72f2e.html'
res = requests.get(url)
res.encoding = 'utf-8'
strk=res.text

fo=open("str.txt","w")
fo.write(strk)
fo.close()

need=re.finditer(
	r"https://wkimg.bdimg.com/img/.*?new=1&w=500&p=1",
	strk)

for match in need:
	print(match.group())
