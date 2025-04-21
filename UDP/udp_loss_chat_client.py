# 코드 수정 필요
from socket import *

BUFF_SIZE = 1024
port = 3333

c_sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('-> ')
    reTx = 0

    while reTx < 5:
        resp = str(reTx) + ' ' + msg
        c_sock.sendto(resp.encode(), ('localhost', port))

        c_sock.settimeout(2)
        try:
            data, addr = c_sock.recvfrom(BUFF_SIZE)
        except timeout:
            reTx += 1
            print('Timeout 발생! 재전송 {}회'.format(reTx))
            continue
        else:
            break

    c_sock.settimeout(None)
    data, addr = c_sock.recvfrom(BUFF_SIZE)
    print('<- ',data.decode())
    c_sock.sendto(b'ack', addr)