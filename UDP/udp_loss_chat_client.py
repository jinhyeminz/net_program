# 코드 수정 완료
from socket import *
import random

port = 3333
BUFF_SIZE = 1024

c_sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('-> ')
    reTx = 0

    while reTx <= 5:
        resp = str(reTx) + ' ' + msg
        c_sock.sendto(resp.encode(), ('localhost', port))
        c_sock.settimeout(2)
        try:
            data, addr = c_sock.recvfrom(BUFF_SIZE)
        except timeout:
            reTx += 1
            print(f'재전송 {reTx}회')
            continue
        else:
            print(data.decode())
            break

    c_sock.settimeout(None)

    while True:
        data, addr = c_sock.recvfrom(BUFF_SIZE)
        if random.random() <= 0.5:
            continue
        else:
            c_sock.sendto(b'ack', addr)
            print('<- ', data.decode())
            break