import socket
import time

BUF_SIZE = 1024

sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock1.connect(('localhost', 6666))
sock2.connect(('localhost', 6667))

f = open("data.txt", "w")

print("Enter command: 1, 2, quit")

while True:
    cmd = input(">> ")

    if cmd == '1':
        sock1.send(b'Request')
        data = sock1.recv(BUF_SIZE).decode()
        temp, humid, illum = data.split(',')
        now = time.ctime(time.time())
        log = f"{now}: Device1: Temp={temp}, Humid={humid}, Iilum={illum}"
        print(log)
        f.write(log + '\n')

    elif cmd == '2':
        sock2.send(b'Request')
        data = sock2.recv(BUF_SIZE).decode()
        hb, steps, cal = data.split(',')
        now = time.ctime(time.time())
        log = f"{now}: Device2: Heartbeat={hb}, Steps={steps}, Cal={cal}"
        print(log)
        f.write(log + '\n')

    elif cmd == 'quit':
        sock1.send(b'quit')
        sock2.send(b'quit')
        print("Connections closed")
        break

    else:
        print("Please enter a valid command.")

f.close()
sock1.close()
sock2.close()
