from socket import *

BUFF_SIZE = 1024
port = 9000

address = ('http:/www.daum.net', 80)

s_sock = socket(AF_INET, SOCK_STREAM)
s_sock.bind(('', port))
s_sock.listen(1)

c_sock = socket(AF_INET, SOCK_STREAM)

while True:
    conn, addr = s_sock.accept()
    data = conn.recv(BUFF_SIZE)
    if not data:
        conn.close()
        continue
    
    msg = data.decode()

    req = msg.split('\r\n')[0]
    req += '\r\nHost: www.daum.net\r\n'
    req += '\r\n'

    c_sock.connect(('www.daum.net', 80))
    c_sock.send(req.encode('utf-8'))

    conn.send(c_sock.recv(BUFF_SIZE))