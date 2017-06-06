import socket,threading

def tcplink(csocket,addr):   
    while True:
        data=csocket.recv(1024)
        print(data)
        if not data or data.decode('utf-8')=='exit':
            break
        csocket.send((data.decode('utf-8')+'huu').encode('utf-8'))
    csocket.close()
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',8081))
server.listen(5)
while True:
    csocket,addr=server.accept()
    t=threading.Thread(target=tcplink,args=(csocket,addr))
    t.start()
server.close()

