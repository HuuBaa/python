from bs4 import BeautifulSoup
import re
htmldata='''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister huu huu" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
'''
soup=BeautifulSoup(htmldata,"html.parser")
#print(soup.prettify())
# print(soup.find('p',{'class':'title'}).contents)
# print(soup.find('a',id='link2')['class'])
# print(soup.head.get_text())

# data=soup.find_all(re.compile(r'^b'))
# for tag in data:
#     print(tag.name)
print(soup.find_all('a',href=re.compile(r'http://example\.com/')))

# print(soup.find_all('p',class_=re.compile(r'title')))

# def has_six_characters(css_class):
#     return css_class is not None and len(css_class) == 5

# print(soup.find_all(class_=has_six_characters))