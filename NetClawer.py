import urllib
from urllib import request  
url ="https://www.cnblogs.com/Axi8/p/5757270.html"
request = urllib.request.Request(url)
htmlcode = urllib.request.urlopen(request).read()
print("net code>>>\n", htmlcode)
with open(r"file\html1.html", "w") as file:
    file.write(htmlcode.decode("GBK"))
