#!/bin/python3 
from socket import *
import struct
from time import sleep

def udp_server_broadcast():
    '''
    message format:
    struct msg{
        unsiged int type,   // 4 bytes
        char data[],
    }
    '''
    PORT = 55781
    BROADCAST = "<broadcast>"
    MY_IP = "192.168.42.255"
    MEG_TYPE=1;
    msg = struct.pack("B12s", MEG_TYPE, MY_IP.encode('utf-8'))

    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(('',0))
    sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    brocadcast_addr = (BROADCAST, PORT)

    while True:
        sock.sendto(msg, brocadcast_addr)
        sleep(1)

if __name__ == "__main__":
    udp_server_broadcast()
