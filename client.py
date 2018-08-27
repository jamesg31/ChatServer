import socket
import os
import threading

s = socket.socket()
os.system('cls')
print('Welcome to the Chat Room!')
username = input('Username: ')
history = []
log_size = 50

def printHistory():
    os.system('cls')
    for i in history[-log_size:]:
        print(str(i))

def main():
    host = input('IP Address: ')
    if host == 'localhost':
        host = socket.gethostname()
    port = input('Port: ')
    try:
        s.connect((host, int(port)))
    except:
        print('Connection Error')
        main()
    history.append('Connected To ' + host)
    printHistory()

main()
s.sendall(username.encode())

def inputSend():
    while True:
        inputdata = input()
        s.sendall(inputdata.encode())
        history.append(username + ': ' + inputdata)
        printHistory()

while True:
    threading.Thread(target=inputSend).start()
    data = s.recv(1024).decode()
    if data != '':
        history.append(data)
        printHistory()
