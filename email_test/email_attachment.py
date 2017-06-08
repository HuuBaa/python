from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr,formataddr
import smtplib


from_addr='18761891778@163.com'
password='hubang1994'
to_addr='742790905@qq.com'
smtp_server='smtp.163.com'
def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

msg=MIMEMultipart('alternative')
msg['From']=_format_addr('python小白<%s>'%from_addr)
msg['to']=_format_addr('python小白<%s>'%to_addr)
msg['Subject']=Header('来自pyt的问候','utf-8').encode()

msg.attach(MIMEText('alternative', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>','html','utf-8'))
with open('../huaji.jpg','rb') as f:
    mime = MIMEBase('image','jpeg',filename='huaji.jpg')

    mime.add_header('Content-Disposition', 'attachment', filename='huaji.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime) 

server=smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
