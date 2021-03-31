### GOKHAN HAS - 161044067 ###
###### CSE 476 - LAB 01 ######

from socket import *
import sys


if __name__ == '__main__':
    server_host = sys.argv[1]
    server_port = sys.argv[2]
    filename = sys.argv[3]

    host_port = server_host  + ":" +server_port
    print("HOST INFORMATION : " + host_port)
    try:
        client_socket = socket(AF_INET,SOCK_STREAM)
        client_socket.connect((server_host,int(server_port)))
        client_socket.send(filename.encode())

    except IOError:
        sys.exit(1)

    response_str = ""
    response_message = client_socket.recv(1024)
    while response_message:
        response_str += response_message.decode()
        response_message = client_socket.recv(1024)

    print("HTML CONTENT : \n" + response_str)
    client_socket.close()

