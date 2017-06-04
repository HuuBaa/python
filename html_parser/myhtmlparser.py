from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super(MyHTMLParser,self).__init__()
        self.tag=''

        self.flag_h3=''
        self.flag_a=''
        self.name=''

        self.flag_time=''
        self.time=''
        self.tmp=''

        self.flag_loc=''
        self.loc=''
    def handle_starttag(self, tag, attrs):
        self.tag=tag
        if self.tag=='h3' and attrs:
            for key,val in attrs:
                if key=="class" and val=='event-title':
                    self.flag_h3=True
        if self.tag=='a' and  self.flag_h3:
            self.flag_a=True  

        if self.tag=='time' :
            self.flag_time=True
            self.tmp=''

        if self.tag=='span' and attrs:
            for key,val in attrs:               
                if key=="class" and val=='event-location':
                    self.flag_loc=True
    def handle_endtag(self, tag):
        if self.flag_h3 and self.flag_a:
            print('会议:',self.name)
            self.flag_a=False
            self.flag_h3=False
        if self.flag_time:
            print('会议时间:',self.time)
            self.flag_time=False
        if self.flag_loc:
            print('会议地点:',self.loc,'\n')
            self.flag_loc=False

    def handle_data(self, data):
        if self.flag_h3 and self.flag_a:
            self.name=data

        if self.flag_time: 
            self.tmp+=data
            self.time=self.tmp

        if self.flag_loc:
            self.loc=data
      
    def handle_startendtag(self, tag, attrs):
        pass    

    def handle_comment(self, data):
        pass

    def handle_entityref(self, name):
        pass

    def handle_charref(self, name):
        pass

with request.urlopen('https://www.python.org/events/python-events/') as f:
    data=f.read()

parser = MyHTMLParser()
parser.feed(data.decode('utf-8'))