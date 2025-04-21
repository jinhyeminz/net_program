from socket import *

BUF_SIZE = 1024
port = 6666

s_sock = socket(AF_INET, SOCK_DGRAM)
s_sock.bind(('', port))
print('Server Listening...')

mbox = {}  # mboxID : [msg1, msg2, msg3, ...]

while True:
    data, addr = s_sock.recvfrom(BUF_SIZE)
    msg = data.decode()

    if msg == 'quit':
        break

    elif msg.startswith('send'):
        _, mboxid, *message = msg.split()
        message = ' '.join(message)

        if mboxid not in mbox:
            mbox[mboxid] = []  # 리스트 생성
        mbox[mboxid].append(message)  # 메시지 추가
        s_sock.sendto(b'OK', addr)

    elif msg.startswith('receive'):
        _, mboxid = msg.split()
        if mboxid in mbox and mbox[mboxid]:
            response = mbox[mboxid].pop(0)  # 제일 먼저 넣은 메시지 꺼내기
            s_sock.sendto(response.encode(), addr)
        else:
            s_sock.sendto(b'No messages', addr)

s_sock.close()
