import requests
from bs4 import BeautifulSoup

if __name__ =="__main__":
    target = "https://www.biqukan.com/1_1094/5403177.html"
    req = requests.get(url=target)
    req.encoding =("GBK")
    content = req.text
    print("encoding:",req.encoding) #内容编码
    print("apparent encoding:",req.apparent_encoding) #头部编码
    # print(content)

    bf = BeautifulSoup(content,"lxml")
    texts = bf.find_all("div",id="content",class_ ="showtxt")
    print(texts)
    #encoding 会改变文件的编码方式

    print(">>"*20)
    texts[0].text.replace("\xa0"*8,"\n\n")
    print(texts)
    with open(r"file\html2","w",encoding="UTF-8") as file:
        file.write(str(texts))