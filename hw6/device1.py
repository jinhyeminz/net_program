import socket
import random

BUF_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 6666))
s.listen(1)
print('Device1 is running...')

conn, addr = s.accept()
print('Connected by:', addr)

while True:
    data = conn.recv(BUF_SIZE).decode()

    if data == 'Request':

        temp = random.randint(0, 40)
        humid = random.randint(0, 100)
        illum = random.randint(70, 150)

        msg = f"{temp},{humid},{illum}"
        conn.send(msg.encode())

    elif data == 'quit':
        print('Quit command received')
        break

conn.close()
s.close()
