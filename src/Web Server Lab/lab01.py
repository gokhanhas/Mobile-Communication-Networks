### GOKHAN HAS - 161044067 ###
###### CSE 476 - LAB 01 ######

server_port = 6787

# import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)

# Fill in start
serverSocket.bind(("", server_port))
serverSocket.listen(2)
print(gethostbyname(gethostname()))
print("Web server is online, port number : ", server_port)
# Fill in end

while True:
    # Establish the connection
    print("Ready to serve...")
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()


        # Send one HTTP header line into socket
        # Fill in start
        connectionSocket.send(bytes('\HTTP/1.1 200 OK\r\n\r\n'.encode()))
        # Fill in end

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(bytes(outputdata[i].encode()))
        connectionSocket.send(b"\r\n")
        connectionSocket.close()

    except IOError:
        # Send response message for file not found
        # Fill in start
        connectionSocket.send(bytes("\HTTP/1.1 404 Not Found\r\n\r\n".encode()))
        connectionSocket.send(bytes("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode()))
        # Fill in end

        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end

        serverSocket.close()
        break
