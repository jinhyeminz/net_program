from socket import *
port = 2500
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
while True:
    msg = input('Enter a message: ')
    if msg == 'q':
        break
    sock.sendto(msg.encode(), ('localhost', port))
    data, addr = sock.recvfrom(BUFFSIZE)
    print('Server says: ', data.decode())
sock.close()