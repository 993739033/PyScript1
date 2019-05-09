import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    target = "https://www.biqukan.com/1_1094/"
    server = 'http://www.biqukan.com/'
    req = requests.get(url=target)
    req.encoding = ("GBK")
    content = req.text
    print("encoding:", req.encoding)  # 内容编码
    print("apparent encoding:", req.apparent_encoding)  # 头部编码
    # print(content)
    bf = BeautifulSoup(content, "lxml")
    div = bf.find_all("div", class_="listmain")
    # print(div)
    a = BeautifulSoup(str(div[0]), "lxml")
    aItems = a.find_all('a')
    for i, a in enumerate(aItems):
        if i < 20:
            print("index:", i, ">>", a.string, server+a.get("href"),"\n")
