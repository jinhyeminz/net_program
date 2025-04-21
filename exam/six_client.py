from socket import *
port = 2500
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
time = 1.0

while True:
    msg = input('Enter a message: ')
    if msg == 'q':
        break
    n = 0
    while True:
        sock.sendto(msg.encode(), ('localhost', port))
        print(f'Packet("{msg}"): Waiting up to {time} secs for ack')
        sock.settimeout(time)
        n += 1
        try:
            data, addr = sock.recvfrom(BUFFSIZE)
        except timeout:
            if n >= 3:
                print("lost message")
                break
        else:
            print('Response ', data.decode())
            break
sock.close()