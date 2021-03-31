### GOKHAN HAS - 161044067 ###
###### CSE 476 - LAB 02 ######

from socket import *

port_number = 12000
ip_adress = "192.168.0.32"

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))


timeout_maximum = 10
timeout_current = 0


while True:
    try:
        serverSocket.settimeout(1.0)
        message, address = serverSocket.recvfrom(1024)
        serverSocket.sendto(message, address)

    except timeout:
        print('Request timed out')
        timeout_current = timeout_current + 1

        if timeout_current >= timeout_maximum:
            print("Heartbeat ...")
            break