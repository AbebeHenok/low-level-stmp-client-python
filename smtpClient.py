from socket import *
import base64
from ssl import SSLContext
import ssl
import os

subject = "SUBJECT: " +input("Enter the subject of the email:")
subject += "\r\n"
msg = input("Enter the message you want to send: ")
# Change the message to the desired one.
# msg = "\r\n This is my message. I am sending this email using Python SMTP client."
endmsg = "\r\n.\r\n"

## Mail server and port ##

#mailServer = 'smtp.gmu.edu'
mailServer = 'smtp.gmail.com'
#mailServer = 'smtp.mail.yahoo.com'
# mailServer = 'smtp.aol.com'
mailPort = 587


## Creating a socket for the client. ##
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailServer, mailPort))
recv = clientSocket.recv(1024)
recv = recv.decode()
if recv[:3] != '220':
        print("220 reply not received from server")

#Send HELO Command and print server response
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024)
print(f"After HELO command " + recv1.decode())
if recv1[:3] != '250':
        print("250 reply not received from server.")

# Start TLS encryption
starttlsCommand = 'STARTTLS\r\n'
clientSocket.send(starttlsCommand.encode())
recv2 = clientSocket.recv(1024).decode()
print("After STARTTLS command: " + recv2)
clientSocket = ssl.wrap_socket(clientSocket)
if recv2[:3] != '220':
    print("220 reply not received after STARTTLS.")

#We must authenticate the user sending the email.
# username = "youremail@gmail.com"
# password = "yourpassword"
username = os.environ.get('SMTP_USERNAME')
password = os.environ.get('SMTP_PASSWORD')
base64_str = ("\x00"+username+"\x00"+password).encode()
base64_str = base64.b64encode(base64_str)
base64_str = base64_str.strip("\n".encode())
authenticate = "AUTH PLAIN ".encode()+base64_str+"\r\n".encode()
clientSocket.send(authenticate)
recv_auth = clientSocket.recv(1024).decode()
print(recv_auth)


#Send MAIL FROM command and print server response
mailFrom = 'MAIL FROM: <{username}>\r\n'
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024)
print("After MAIL FROM command: " +recv2.decode())
if recv2[:3] != '250':
        print("250 reply not received from server from RECV2")

#Send RCPT TO command and print server response
# Change the receiver email address to the desired one.

rcpt = 'RCPT TO: <henok.abebe.ce@gmail.com>\r\n'
clientSocket.send(rcpt.encode())
recv3 = clientSocket.recv(1024).decode()
print("After RCPT TO command: " +recv3)
if recv3[:3] != '250':
        print("250 reply not received from server FROM RECV3")

#Send DATA command and print server respose. 
data = 'DATA\r\n'
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024).decode()
print("After DATA command: " +recv4)
if recv4[:3] != '250':
        print("250 reply not received from server FROM RECV4")

#Send message data
#Change the subject line to the desired one.
# subject = "SUBJECT: Your Subject\r\n"
clientSocket.send(subject.encode())
msgData = msg + endmsg
clientSocket.send(msgData.encode())
recv5 = clientSocket.recv(1024).decode()
print("After sending message: " + recv5)

#Send QUIT command and get server respose
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)
if recv6[:3] != '250':
    print( '250 reply not received from server.' )
#Closing the TCP connection.
clientSocket.close()

