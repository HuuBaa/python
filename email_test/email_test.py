# from email.mime.text import MIMEText
# msg=MIMEText('hello,sent by python','plain','utf-8')
# from_addr='18761891778@163.com'
# password='hubang1994'
# to_addr='742790905@qq.com'
# smtp_server='smtp.163.com'

# msg['From'] = from_addr
# msg['To'] = to_addr
# msg['Subject'] = 'python mail'

# import smtplib
# server=smtplib.SMTP_SSL(smtp_server,465)
# server.set_debuglevel(1)
# server.login(from_addr,password)
# server.sendmail(from_addr,[to_addr],msg.as_string())
# server.quit()

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr

import smtplib

from_addr='18761891778@163.com'
password='hubang1994'
to_addr='742790905@qq.com'
smtp_server='smtp.163.com'
def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

msg=MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>','html','utf-8')
msg['From']= _format_addr('python小白<%s>'%from_addr)
msg['To']= _format_addr('HUU大神<%s>'%to_addr)
msg['Subject']=Header('来自huu的问候','utf-8').encode()
print(msg['From'])
print(msg['To'])
print(msg['Subject'])

server=smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()


