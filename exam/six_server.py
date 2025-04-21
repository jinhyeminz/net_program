from socket import *
import random

port = 2500
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))
print('Listening...')

while True:
    msg, addr = sock.recvfrom(BUFFSIZE)
    if random.randint(1, 10) <= 4:
        print(f'Packet from {addr} lost')
        continue
    print(f'Packet is {msg.decode()} from {addr}')

    sock.sendto(b'ack', addr)