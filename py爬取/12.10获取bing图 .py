import requests,os,urllib
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
url='https://bing.ioliu.cn/'

headers={
	"Referer":"https://cn.bing.com/?form=HPEDGE",
	"User_Agent":"Mozilla/5.0"
}

html=requests.get(url=url,headers=headers)
print(html)
#html.encoding='utf-8'
bs=BeautifulSoup(html.text,'html.parser')
print(bs.select ('img'))

pics_dir='pics'
if not os.path.exists(pics_dir):
    os.mkdir(pics_dir)
all_links=bs.find('img')
for link in all_links:
    src=link.get('src')
    attrs=[src]
    for attr in attrs:
        if attr !=None and ('.jpg' in attr or '.png' in attr):
            full_path=attr
            file_n=full_path.split('/')[-1]
            print("============")
            print("图文件完整路径：",full_path)
            try:
                image=urllib.request.urlopen(full_path)
                f=open(os.path.join(pics_dir,file_n),'wb')
                f.write(image.read())
                print('successful download %s'%(file_n))
                f.close()
            except:
                print("无法下载：%"%(file_n))
