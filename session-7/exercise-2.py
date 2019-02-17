# Programming our second client running in a loop.

import socket

PORT = 8080
IP = "127.0.0.1"

# Creating a while loop for communicating with the server infinite times.
while True:
    # Creating a socket for communicating with the server.
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    print("Socket created")

    message = input("Please send me a message: ")

    #Connect to the server
    s.connect((IP, PORT))


    s.send(str.encode(message))

    msg = s.recv(2048).decode("utf-8")

    print("MESSAGE FROM THE SERVER")
    print(msg)
    s.close()
    print("The end")
