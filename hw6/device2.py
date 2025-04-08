# device2.py
import socket
import random

BUF_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 6667))
s.listen(1)
print('Device2 is running...')

conn, addr = s.accept()
print('Connected by:', addr)

while True:
    data = conn.recv(BUF_SIZE).decode()

    if data == 'Request':
        hb = random.randint(40, 140)
        steps = random.randint(2000, 6000)
        cal = random.randint(1000, 4000)
        msg = f"{hb},{steps},{cal}"
        conn.send(msg.encode())

    elif data == 'quit':
        print('Quit command received')
        break

conn.close()
s.close()
