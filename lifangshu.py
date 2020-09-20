from bs4 import BeautifulSoup
import requests

def download_img(url_img,name_img):
    img_text = requests.get(url_img)
    img = img_text.content
    path = r'XXXXXX\%s.png'%(name_img)      #XXXXXX处为需要保存的绝对路径
    with open(path, 'ab') as f:
        f.write(img)
        f.close()
url = 'http://29.s.bookln.cn/qr.html?crcode=XXXXXXXX' # 在这里写下你从立方书中获取到的教材链接
req = requests.get(url)
req.close()
req.encoding = 'utf-8'
html = req.text
soup = BeautifulSoup(html,features="html.parser")
n = 0
for i in soup.find_all('img',class_="thumb-img"):
    n = int(n) + 1
    url_this = i.get('src')
    print(i.get('src'))
    name_img = str(n)
    download_img(url_this, name_img)
print("Done!")