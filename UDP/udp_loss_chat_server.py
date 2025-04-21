# 코드 수정 필요
from socket import *
import random
import time

port = 3333
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

while True:
    sock.settimeout(None) # 소켓의 블로킹 모드 timeout 설정, 무한정 블로킹
    while True:
        data, addr = sock.recvfrom(BUFF_SIZE) # 메시지 수신
        if random.random() <= 0.5: # 50퍼센트 확률로 응답 안함
            continue
        else: # 응답함
            sock.sendto(b'ack', addr)
            print('<-', data.decode())
            break

    msg = input('-> ')
    reTx = 0

    while reTx <= 5:
        resp = str(reTx) + ' ' + msg
        sock.sendto(resp.encode(), ('localhost', port))
        sock.settimeout(2)
        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
        except timeout:
            reTx += 1
            print('재전송 {}회'.format(reTx))
            continue
        else:
            break