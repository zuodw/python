import socket
from time import ctime

HOST = ''
PORT = 21568
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpSerSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('wating for message...')
    data, addr = udpSerSock.recvfrom(BUFSIZE)
    if not data:
        break
    udpSerSock.sendto(b'[%s] %s' % (ctime().encode('utf-8'), data), addr)
    print('...received from and returned to: ', addr)

udpSerSock.close()