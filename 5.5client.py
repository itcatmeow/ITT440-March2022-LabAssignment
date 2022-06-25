import socket
import sys

s = socket.socket()

port = 8080

s.connect(('192.168.56.105',port))

file = open('test.txt', 'r')
data = file.read()

s.send('test.txt'.encode("utf-8"))

msg = s.recv(1024).decode("utf-8")

print(f'[Server]: {msg}')

s.send(data.encode("utf-8"))

msg = s.recv(1024).decode("utf-8")

print(f'[Server]: {msg}')

file.close()
s.close()

