### GOKHAN HAS - 161044067 ###
###### CSE 476 - LAB 01 ######


import threading
from socket import *
import sys

serverPort = 8080

# A Thread class has been written using the threading library. This class is written in the run method when threads in the threading library are created.
# Run method is overridden.
class Thread(threading.Thread):
    def __init__(self, connect, address):
        threading.Thread.__init__(self)
        self.connectionSocket = connect
        self.addr = address

    def run(self):
        try:
            # The connection is trying to be established.
            fileName = self.connectionSocket.recv(1024)

            if not fileName:
                print("ERROR ! Filename does not exits ...")
                sys.exit(1)
            data = ""
            if sys.getsizeof(fileName) < 50: # connection from terminal ...
                f = open(fileName)
                data = f.read()
            else: # connection from browser
                self.connectionSocket.send(bytes('\HTTP/1.1 200 OK\r\n\r\n'.encode()))
                filename = fileName.split()[1]
                f = open(filename[1:])
                data = f.read()

            print("SENDING HTML FILE: \n" + data)
            print("\n")

            # Content in the HTML file is sent.
            for i in range(0, len(data)):
                self.connectionSocket.send(bytes(data[i].encode()))
            self.connectionSocket.send(b"\r\n")
            self.connectionSocket.close()

        except IOError:
            # If an error occurs, the connection must be closed.
            self.connectionSocket.send(bytes("HTTP/1.1 404 Not Found\r\n\r\n".encode()))


def main():
    global serverPort
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(5)
    threads = []
    print('MultiThread Server Is Running ...')

    while True:
        # Establish the connection
        connectionSocket, addr = serverSocket.accept()
        print("ADDRESS: " , addr)
        print("\n")
        client = Thread(connectionSocket, addr)
        client.start()
        threads.append(client)

    serverSocket.close()

if __name__ == '__main__':
    main()