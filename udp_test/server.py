import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9998))
while True:
    data,addr=s.recvfrom(1024)
    print('receive from %s%s'%addr)
    s.sendto((b'Hello,%s!'%data),addr)
