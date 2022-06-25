import socket
import sys

s = socket.socket()
print("Socket successfully created")

port = 8080

s.bind(('',port))
print("socket binded to " + str(port))

s.listen(5)
print("socket is listening")

while True:
        c,addr = s.accept()
        print("Got connection from" + str(addr))

        filename = c.recv(1024).decode("utf-8")
        print(f'[RECV] Receiving the filename')
        file = open(filename, "w")
        c.send(f'Filename received.'.encode("utf-8"))

        data = c.recv(1024).decode("utf-8")
        print(f'[RECV] Receiving the file data.')
        file.write(data)
        c.send(f'File data received'.encode("utf-8"))
        file.close()

c.close()
