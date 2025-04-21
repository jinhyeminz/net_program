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
    # req = msg.split('\r\n')[0]
    req = 'GET / HTTP/1.1\r\n'
    req += 'Host: www.daum.net\r\n'

    c_sock.connect(('www.daum.net', 80))
    c_sock.send(req.encode('utf-8'))

    s_sock.send(c_sock.recv(BUFF_SIZE))