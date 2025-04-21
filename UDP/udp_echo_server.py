from socket import *

port = 2500
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

while True:
    msg, addr = sock.recvfrom(BUFFSIZE)
    print('Received: ', msg.decode())
    sock.sendto(msg, addr)