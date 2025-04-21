from socket import *

BUFF_SIZE = 1024
port = 5555

c_sock = socket(AF_INET, SOCK_DGRAM)
c_sock.connect(('localhost', port)) 
# 보낼 때마다 주소 붙이는게 번거롭기 때문에 사용하기 편하게 하는 것
# 실제로 포트에 연결되는건 아님
# UDP에서 connect를 쓰면 send, recv로 써도 됨 
# 서버가 IP주소랑 포트 번호 아니까

for i in range(10):
    time = 0.1   # 10번 전송
    data = 'Hello, IoT' # 0.1초
    while True:
        c_sock.send(data.encode())
        print('Packet({}): Waiting up to {} secs for ack'.format(i, time))
        c_sock.settimeout(time)
        try:
            data = c_sock.recv(BUFF_SIZE)
        except timeout:
            time *= 2 # 대기시간 2배 증가
            if time > 2.0: # 최대 대기시간 초과
                break
        else:
            print('Response', data.decode())
            break