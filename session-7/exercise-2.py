# Programming our second client.

import socket

#Creating a socket for communicating with the server.
s = socket.socket(socket. AF_INET, socket.SOCK_STREAM) #Creating a socket for communicating through Internet. Always these parameters.

print("Socket created")

PORT = 8080
IP = "212.128.253.88"

while True:

    message = input("Please send me a message: ")

    #Connect to the server
    s.connect((IP, PORT))


    s.send(str.encode(message))

    msg = s.recv(2048).decode("utf-8")

    print("MESSAGE FROM THE SERVER")
    print(msg)
    s.close
    print("The end")
