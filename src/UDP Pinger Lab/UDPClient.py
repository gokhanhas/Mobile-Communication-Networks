### GOKHAN HAS - 161044067 ###
###### CSE 476 - LAB 02 ######

from socket import *
import time

# initialize socket adress parameters
port_number = 12000
ip_adress = "192.168.0.10"

# Create a UDP socket by using SOCK_DGRAM
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Set the timeout, if the server is not responding (second)
clientSocket.settimeout(1)
socket_addr = (ip_adress, port_number)

# Send ping for 10 times
for i in range(10):
    first_time = time.time()
    # Message Format in assignment pdf : Ping sequence_number time
    msg = 'Ping ' + str(i + 1) + " " + str(time.strftime("%H:%M:%S"))
    # Send datagram
    clientSocket.sendto(bytes(msg.encode()), socket_addr)

    try:
        data, server = clientSocket.recvfrom(1024)
        second_time = time.time()
        rtt = second_time - first_time
        print("Message has been received : ", data.decode())
        print("RTT is                    : ", rtt)

    except timeout:
        print('Request timed out')
