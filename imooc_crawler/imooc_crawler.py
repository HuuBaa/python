# from urllib import request

# req=request.Request('http://www.baidu.com')
# req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0')
# res=request.urlopen(req)
# print(res.read().decode('utf-8'))

from urllib.request import urlopen,Request
from urllib import parse
req=Request('http://www.thsrc.com.tw/tw/TimeTable/SearchResult')
postData=parse.urlencode([
    ('StartStation','2f940836-cedc-41ef-8e28-c2336ac8fe68'),
    ('EndStation','977abb69-413a-4ccf-a109-0272c24fd490'),
    ('SearchDate','2017/06/11'),
    ('SearchTime','12:30'),
    ('SearchWay','DepartureInMandarin')
    ])
req.add_header('Origin','http://www.thsrc.com.tw')
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36')
res=urlopen(req,data=postData.encode('utf-8'))
print(postData)
print(postData.encode('utf-8'))
#print(res.read().decode('utf-8'))