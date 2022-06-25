import socket

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
print("Berjaya buat sokett")

port = 8888

s.bind(("",port))
print("Berjaya bind soket di port: " + str(port))

s.listen(5)
print("soket tengah menunggu client!")

while True:
        bytesAddressPair = s.recvfrom(1024)

        message = bytesAddressPair[0]
        address = bytesAddressPair[1]

        clientMessage = "Client cakap: {}".format(message)
        clientIP = "IP address client: {}".format(address)

        print(clientMessage)
        print(clientIP)

        s.sendto("Terima Kasih")

c.close()


