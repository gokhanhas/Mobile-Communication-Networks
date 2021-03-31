### GOKHAN HAS - 161044067 ###
###### CSE 476 - LAB 03 ######

from socket import *
import ssl
import base64

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"


# Choose a mail server (e.g. Google mail server) and call it mailserver
# Fill in start
mailserver = ('smtp.gmail.com', 465)    # The port TLS is 465
# Fill in end

# Create socket called clientSocket and establish a TCP connection with mailserver
# Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket = ssl.wrap_socket(clientSocket)    # I used in TLS in this code.
clientSocket.connect(mailserver)
# Fill in end

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(bytes(heloCommand.encode()))
recv1 = clientSocket.recv(1024)
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

authCommand = base64.b64encode('\x00gokhan2434has\x00gokhanhas'.encode())
clientSocket.send(('AUTH PLAIN ' + authCommand.decode() + '\r\n').encode())
authResponse = clientSocket.recv(1024)
print(authResponse)

# Send MAIL FROM command and print server response.
# Fill in start
mailFromCommand = 'MAIL FROM: <gokhan2434has@gmail.com>\r\n'
clientSocket.send(mailFromCommand.encode())
mailFromResponse = clientSocket.recv(1024).decode()
print(mailFromResponse)
if mailFromResponse[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
rcptToCommand = 'RCPT TO: <gokhan1has@gmail.com>\r\n'
clientSocket.send(rcptToCommand.encode())
rcptToResponse = clientSocket.recv(1024).decode()
print(rcptToResponse)
if rcptToResponse[:3] != '250':
    print('250 reply not received from server')
# Fill in end

# Send DATA command and print server response.
# Fill in start
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
dataResponse = clientSocket.recv(1024).decode()
print(dataResponse)
if dataResponse[:3] != '354':
    print('354 reply not received from server')
# Fill in end

# Send message data.
# Fill in start
clientSocket.send(msg.encode())
# Fill in end

# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg.encode())
# Fill in end

# Send QUIT command and get server response.
# Fill in start
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
quitResponse = clientSocket.recv(1024).decode()
print(quitResponse)
# Fill in end
