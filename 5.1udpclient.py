import socket

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

port = 8888

s.sendto("Hi,saya client. Terima Kasih!",('192.168.56.105', port))

data = s.recvfrom(1024)

print(data)

s.close()





