import socket
import sys
import time
import errno
import math
from multiprocessing import Process

logmsg = 'You have chosen Logarithm\n'
sqrtmsg = 'You have chosen Square Root\n'
expmsg = 'You have chosen Exponential\n'

def process_start(s_sock):
        s_sock.send(str.encode('Calculator'))
        while True:
                data = s_sock.recv(2048).decode()
                if data == '1':
                        s_sock.sendall(str.encode(logmsg))
                        number = s_sock.recv(2048).decode()
                        num = int(number)
                        calculate = math.log10(num)
                        result = str(calculate)
                        s_sock.sendall(str.encode(result))
                elif data == '2':
                        s_sock.sendall(str.encode(sqrtmsg))
                        number = s_sock.recv(2048).decode()
                        num = int(number)
                        calculate = math.sqrt(num)
                        result = str(calculate)
                        s_sock.sendall(str.encode(result))
                elif data == '3':
                        s_sock.sendall(str.encode(expmsg))
                        number = s_sock.recv(2048).decode()
                        num = int(number)
                        calculate = math.exp(num)
                        result = str(calculate)
                        s_sock.sendall(str.encode(result))
                else:
                        break
        s_sock.close()

if __name__=='__main__':
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind(("",8888))
        print("listening...")
        s.listen(3)
        try:
                while True:
                        try:
                                s_sock,s_addr = s.accept()
                                p = Process(target=process_start, args=(s_sock,))
                                p.start()



                        except socket.error:
                                print('got a socket error')

        except Exception as e:
                print('an exception occured!')
                print(e)
                sys.exit(1)
        finally:
                s.close()


