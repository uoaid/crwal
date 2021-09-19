import requests
from bs4 import BeautifulSoup
import re
import os


# 伪造请求头: 基操
Hostreferer = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
}


response = requests.get("http://www.jianshu.com/p/23791264077f", headers=Hostreferer)
home_page = response.content.decode()

# html 解析
soup = BeautifulSoup(home_page, "html.parser")

# 保存链接
list = []
re1 = re.compile(r'data-original-src="//(.*?)"')
for item in soup.find_all('div', class_='image-view'):
    res = re.findall(re1, str(item))
    # print(res)
    list.append(res)

path = r'D:\code\python_temp\flask_demo\static\img';   # 保存路径名

num = 1
for i in list:
    a = 'http://'
    for j in i: a += j
    print(a)
    img = requests.get(a, headers=Hostreferer)
    file_name = os.path.join(path, str(num) + '.jpg')
    print(img)

    with open(file_name, 'wb') as f:
        f.write(img.content)
    num = num + 1
