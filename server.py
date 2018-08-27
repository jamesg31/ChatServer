import socket
import threading

port = input('Port: ')
s = socket.socket()
host = socket.gethostname()
s.bind((host, int(port)))
s.listen(5)
print('Server created on IP: ' + socket.gethostbyname(host) + ' Port: ' + port)
clients = []

def client(c, clients):
    while True:
        data = c.recv(1024).decode()
        data = usernames[c].decode() + ': ' + data
        for x in clients:
            if x != c:
                if testConnection(x, clients):
                    x.send(data.encode())

def testConnection(client, clients):
    try:
        client.send(''.encode())
        return True
    except:
        print('Client Disconnected')
        clients.remove(client)
        return False

usernames = {}

while True:
   c, addr = s.accept()
   print('Got connection from', addr)
   clients.append(c)
   username = c.recv(1024)
   usernames[c] = username
   for x in clients:
       if testConnection(x, clients):
           x.send((username.decode() + ' connected.').encode())

   t = threading.Thread(target=client, args=(c, clients,))
   t.start()
c.close()
