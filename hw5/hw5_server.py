from socket import *

s = socket()
s.bind(('', 80))
s.listen(10)
print("웹 서버 켜짐")

while True:
    c, addr = s.accept()

    print("클라이언트 연결 성공")

    data = c.recv(1024)
    if not data:
        c.close()
        continue

    msg = data.decode()
    req = msg.split('\r\n')[0]

    try:
        method, path, _ = req.split()
        filename = path[1:]

        if filename == 'index.html':
            header = 'HTTP/1.1 200 OK\r\n'
            header += 'Content-Type: text/html; charset=euc-kr\r\n'
            header += '\r\n'
            c.send(header.encode())
            f = open(filename, 'r', encoding='utf-8')
            data = f.read()
            c.send(data.encode('euc-kr'))

        elif filename == 'iot.png':
            header = 'HTTP/1.1 200 OK\r\n'
            header += 'Content-Type: image/png\r\n'
            header += '\r\n'
            c.send(header.encode())
            f = open(filename, 'rb')
            data = f.read()
            c.send(data)

        elif filename == 'favicon.ico':
            header = 'HTTP/1.1 200 OK\r\n'
            header += 'Content-Type: image/x-icon\r\n'
            header += '\r\n'
            c.send(header.encode())
            f = open(filename, 'rb')
            data = f.read()
            c.send(data)

        else:
            c.send(b'HTTP/1.1 404 Not Found\r\n\r\n')
            c.send(b'<html><head><title>Not Found</title></head>')
            c.send(b'<body>Not Found</body></html>')

    except:
        c.send(b'HTTP/1.1 404 Not Found\r\n\r\n')
        c.send(b'<html><head><title>Not Found</title></head>')
        c.send(b'<body>Not Found</body></html>')

    c.close()
