#!/usr/bin/env python

import socket


def main():
    serv = setup()
    while True:
        (csock,addr) = serv.accept()  # <1>
        handle_client(csock)

def setup():
    serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # <2>
    serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # <3>

    serv.bind((socket.gethostname(),7777))  # <4>

    serv.listen(5) # <5>

    return serv


def handle_client(cli_sock):
    request = cli_sock.recv(1024) # <6>
    
    reply = request.upper()[::-1]  # <7>

    cli_sock.sendall(reply) # <8>
    cli_sock.close() # <9>
       
if __name__ == '__main__':
    main()
