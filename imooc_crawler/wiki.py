from urllib.request import urlopen
import re
from bs4 import BeautifulSoup

res=urlopen('https://en.wikipedia.org/wiki/Main_Page').read().decode('utf-8')
soup=BeautifulSoup(res,'html.parser')
listurl=soup.find_all('a',href=re.compile(r'^/wiki/'))

for url in listurl:
    if not re.search(r'(jepg|svg|png|jpg)$',url['href']):
        print(url.get_text(),'>>>>>','https://en.wikipedia.org'+url['href'])
