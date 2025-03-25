import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)

msg = sock.recv(1024)
print(msg.decode())

sock.send(b'Hyemin Jin') # 1 : 이름 전송
 
number = int.from_bytes(sock.recv(1024), 'big')
print(number)

sock.close()
