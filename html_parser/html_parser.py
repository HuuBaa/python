# -*- coding:utf-8 -*-
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)
        print('%s',attrs)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        name = chr(name2codepoint[name])
        print('&%s;' % name)

    def handle_charref(self, name):
        if name.startswith('x'):
            name = chr(int(name[1:], 16))
        else:
            name = chr(int(name))
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&#247&nbsp&copy;tutorial...<br>END</p>
</body></html>''')