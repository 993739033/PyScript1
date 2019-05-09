from bs4 import BeautifulSoup
import requests, sys


class download():
    def __init__(self):
        self.server = "http://www.biqukan.com/"
        self.target = "https://read.douban.com/column/32147842/?icn=from-author-page"
        self.names = []  # 章节名
        self.urls = []  # 章节链接
        self.nums = 0  # 章节数

    # 获取所有下载地址 这里我加了限制
    def getDownUrl(self):
        req = requests.get(url=self.target)
        req.encoding = ("GBK")
        html = req.text
        div_bf = BeautifulSoup(html, "lxml")
        div = div_bf.find_all("div", id='main')
        a_bf = BeautifulSoup(str(div[0]),"lxml")
        a = a_bf.find_all("h3")
        self.nums = len(a)
        for item in a:
            self.names.append(item.string)
            self.urls.append(self.server + item.get("href"))
        print(self.names)
        print(self.urls)


    def getContents(self, target):
        req = requests.get(url=target)
        req.encoding = "GBK"
        html = req.text
        bf = BeautifulSoup(html, "lxml")
        texts = bf.find_all('div', class_='showtxt')
        try:
            itemtexts = texts[0].text.replace('\xa0' * 8, '\n\n')
        except Exception as e:
            print(e)
        return itemtexts

    def writer(self, name, path, text):
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')

if __name__ == "__main__":
    dl = download()
    dl.getDownUrl()
    # print('《一年永恒》开始下载：')
    # for i in range(dl.nums):
    #     dl.writer(dl.names[i], '一念永恒.txt', dl.getContents(dl.urls[i]))
    #     sys.stdout.write("  已下载:%.3f%%" % float((i) / dl.nums) + '\r')
    #     print("  已下载:%.3f%%" % float((i) / dl.nums) + '\r')
    #     sys.stdout.flush()
    # print('《一年永恒》下载完成')
