import urllib.request
import re
req=urllib.request.urlopen('http://coding.imooc.com/')
buf=req.read()
buf = buf.decode('utf-8')
listurl=re.findall(r'http://szimg\.mukewang\.com/.+\.jpg',buf)
print(listurl)
i=0
for urlitem in listurl:
    with open('str'+str(i)+'.jpg','wb') as f:
        request=urllib.request.urlopen(urlitem)
        buff=request.read()
        f.write(buff)
    i=i+1