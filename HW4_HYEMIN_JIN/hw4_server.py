from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)
print('waiting...')

while True:
    client, addr = s.accept()
    result = ""
    print('connection from ', addr)
    while True:
        data = client.recv(1024).decode() # 전송 받은 데이터, 문자형으로 변환
        if not data: # 데이터 없을 시 종료
            break

        try:
            data = data.split()
        except:
            client.send(b'Try again')
        else:
            a = int(data[0])
            b = int(data[2])

            if a >= b:
                if data[1] == '+':
                    result = a + b
            
                elif data[1] == '-':
                    result = a - b

                elif data[1] == '*':
                    result = a * b

                elif data[1] == '/':
                    result = round(a / b, 1)
            
            else:
                if data[1] == '+':
                    result = a + b
            
                elif data[1] == '-':
                    result = b - a

                elif data[1] == '*':
                    result = a * b

                elif data[1] == '/':
                    result = round(b / a, 1)

            result = str(result)
            client.send(result.encode())

    client.close()