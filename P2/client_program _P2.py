#Client program for asking the user a sequence and sending the reverse-complement to the server.
import socket

#Importing class Seq
from Seq import Seq


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

    #Creating our object of class Seq and passing user sequence as a parameter.
    client_sequence = Seq(sequence)

    #Calling reverse method.
    reverse_seq = client_sequence.reverse()

    #Calling complement method.
    rev_complement = Seq(reverse_seq).complement()

    #Encoding the message and sending it to the server.
    s.send(str.encode(rev_complement))

    msg = s.recv(2048).decode("utf-8")

    print("MESSAGE FROM THE SERVER")
    print(msg)
    s.close()
    print("The end")