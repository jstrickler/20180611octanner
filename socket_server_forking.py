#!/usr/bin/env python

import socket
import os

def setup():
    serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # serv.setblocking(0)
    
    serv.bind((socket.gethostname(),7777))
    
    serv.listen(5)
    
    return serv

def main():
    serv = setup()
    while True:
        (csock,addr) = serv.accept()
        handle_client(csock)

def handle_client(cli_sock):
    pid = os.fork()
    if pid:
        return
    request = cli_sock.recv(1024)
    
    reply = request.upper()[::-1]  # upper & reversed

    cli_sock.sendall(reply)
    cli_sock.close()
       
if __name__ == '__main__':
    main()