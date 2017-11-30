import socket

HOST, PORT = '127.0.0.1', 9995

udpSockClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = bytes(input('> '), 'utf-8')

udpSockClient.sendto(data, (HOST, PORT))

udpSockClient.recv(1024)