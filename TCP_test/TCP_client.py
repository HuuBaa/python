import socket,time
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',8081))
client.send(b'test')
client.send(b'test1')
client.send(b'test2')
data=client.recv(1024)
print(data)
client.close()