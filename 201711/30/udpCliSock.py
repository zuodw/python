import socket

HOST = '127.0.0.1'
PORT = 21568
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpCliSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = input('> ')
    if not data:
        break
    udpCliSock.sendto(data.encode('utf-8'), ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZE)
    if not data:
        break
    print(data)

udpCliSock.close()