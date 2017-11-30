#encoding=utf-8
import socket
from time import ctime

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connecting...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connecting from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZE)
        if not data:
            break
        tcpCliSock.send(b'[%s] %s' % (ctime().encode('utf-8'), data))
    tcpCliSock.close()
tcpSerSock.close()