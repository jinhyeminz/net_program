from socket import *

BUF_SIZE = 1024
port = 6666

s_sock = socket(AF_INET, SOCK_STREAM)
s_sock.bind(('', port))
s_sock.listen(1)
print('Listening...')
c, addr = s_sock.accept()
print('connected by', addr)
mbox = {}

while True:
    data = c.recv(BUF_SIZE) # send [mboxID] message, receive [mboxID], quit
    msg = data.decode() 

    if msg == 'quit':
        break

    elif msg.startswith('send'):
        _, mboxid, *message = msg.split()
        message = ' '.join(message)

        if mboxid not in mbox:
            mbox[mboxid] = []
            
        mbox[mboxid].append(message)
        c.send(b"OK")

    elif msg.startswith('receive'):
        _, mboxid = msg.split()
        if mboxid in mbox and mbox[mboxid]:
            rep = mbox[mboxid].pop(0)
            c.send(rep.encode())
        else:
            c.send(b'No messages')
            
c.close()
s_sock.close()