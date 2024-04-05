# print("Hello I am RTDS")
# import sys
# print("Welcome to ", str(sys.argv[1]))

import socket
import time
import struct

TCP_IP = '172.24.9.249'
TCP_PORT = 4575
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

start = time.clock()
for i in range(1,101):
 f = float(i) + 0.15
 send_data_str = struct.pack('>if',i, f)
 s.send(send_data_str)
 recv_data_str = s.recv(BUFFER_SIZE)
 recv_data_str_unpacked = struct.unpack('>if',recv_data_str)
 j = int(recv_data_str_unpacked[0])
 t = float(recv_data_str_unpacked[1])
 print ("The j returned is: ", j)
 print ("The t returned is: ", t)
 time.sleep(1) #This sleep is needed for the ClosePort() below

s.close()
print ('All iterations complete.')
finish = time.clock() - start
print ('The execution time is %fs.' %finish)