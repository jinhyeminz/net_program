from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 3333))

while True:
    msg = input('send massage: ')
    if msg == 'q':
        break

    s.send(msg.encode()) # 전송 시 byte 형으로 변환

    print('Received message:', s.recv(1024).decode())

s.close()