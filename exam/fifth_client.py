from socket import *

port = 6666
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', port))

while True:
    msg = input('Enter a message("send mboxId message" or "receive mboxId"):')
    if msg == 'quit':
        break
    sock.send(msg.encode()) # 송신 메세지 보내기

    data = sock.recv(BUFFSIZE)
    
    print(data.decode())

sock.close()