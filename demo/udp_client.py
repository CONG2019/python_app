#!/bin/python3 
from socket import *
import struct

def find_server():
    HOST = "255.255.255.255"
    PORT = 55781
    BUFSIZE = 1024

    ADDR = (HOST, PORT)

    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(('', PORT))
    while True:
        data, addr = sock.recvfrom(BUFSIZE)
        msg_type, server_ip = struct.unpack("B12s",data)
        print('msg_type=%d, server_ip=%s, current_ip=%s'%(msg_type, server_ip.decode('utf-8'), addr[0]))

    sock.close()


if __name__ == "__main__":
    find_server()

