import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    client.send(b'Hello ' + addr[0].encode())
    
    name = client.recv(1024) # 2 : 이름 수신 후 출력
    print(name.decode())

    student_number = 20221316
    send_number = student_number.to_bytes(4, 'big')

    client.send(send_number)

    client.close()