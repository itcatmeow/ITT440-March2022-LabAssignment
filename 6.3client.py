import socket

ClientSocket = socket.socket()
host = '192.168.56.105'
port = 8888

print('Waiting for connection')
try:
        ClientSocket.connect((host,port))
except socket.error as e:
        print(str(e))

Response = ClientSocket.recv(1024)
print(Response)
while True:
        Input=input('\nChoose a function: [1 for logarithm][2 for square root] [3 for exponential] [0 for quit]\n\n')
        ClientSocket.send(str.encode(Input))
        Response = ClientSocket.recv(1024)
        print(Response.decode('utf-8'))
        num=input('Enter a number: ')
        ClientSocket.send(str.encode(num))
        result = ClientSocket.recv(1024)
        print(result.decode('utf-8'))

ClientSocket.close()

