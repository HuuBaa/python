import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for i in [0,1]:
    s.sendto(b'huu',('127.0.0.1',9998))
    print(s.recv(1024).decode('utf-8'))
s.close()