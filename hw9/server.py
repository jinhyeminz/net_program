import socket
import threading
import time

clients = []

def client_thread(conn, addr):

    print('new client', addr)

    clients.append(conn)

    while True:
        try:
            data = conn.recv(1024)

            if not data:
                break

            message = data.decode()
            if 'quit' in message:
                print(addr, 'exited')
                clients.remove(conn)
                conn.close()
                break

            print(time.asctime() + str(addr) + ': ' + message)

            for client in clients:
                if client != conn:
                    client.send(data)

        except:
            break

    if conn in clients:
        clients.remove(conn)

    conn.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 2500))
s.listen()
print('TCP Server Started')

while True:
    conn, addr = s.accept()
    threading.Thread(target=client_thread, args=(conn, addr)).start()