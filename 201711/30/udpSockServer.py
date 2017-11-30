import socketserver

class MyUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = str(self.request[0], 'utf-8').strip()
        sock = self.request[1]
        print("{} wrote:".format(self.client_address[0]))
        print(data)

        sock.sendto(bytes(data.upper(), 'utf-8'), self.client_address)

if __name__ == '__main__':
    HOST, PORT = '127.0.0.1', 9995
    with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
        server.serve_forever()