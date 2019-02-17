# Client program for sending sequences to the server.
import socket


PORT = 8080
IP = "127.0.0.1"

# Creating a while loop for communicating with the server infinite times.
while True:

    # Creating a socket for communicating with the server.
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Socket created")

    #Asking the user to enter a valid sequence.
    sequence = input("Please enter a valid DNA sequence: ")

    #Connect to the server
    s.connect((IP, PORT))

    #Encoding the sequence entered by the user and sending it to the server.
    s.send(str.encode(sequence))

    msg = s.recv(2048).decode("utf-8")

    print("MESSAGE FROM THE SERVER: ")
    print("The complement sequence is: ", msg)
    s.close()
    print("The end")