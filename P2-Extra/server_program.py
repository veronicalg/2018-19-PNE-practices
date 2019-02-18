# Programming a server program that calculates and returns the complement sequence received from the client.
import socket

#Importing class Seq
from Seq import Seq


# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1"
MAX_OPEN_REQUESTS = 5

# Counting the number of connections
number_con = 0

# Create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serversocket.bind((IP, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        # accept connections from outside
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = serversocket.accept()

        # Another connection!e
        number_con += 1

        # Print the conection number
        print("CONNECTION: {}. From the IP: {}".format(number_con, address))

        # Read the message from the client, if any
        sequence = clientsocket.recv(2048).decode("utf-8")

        # Creating the seq object.
        seq = Seq(sequence)

        # Calling the complement method.
        complement_seq = seq.complement()

        # Sending the complement sequence
        send_bytes = str.encode(complement_seq)

        # We must write bytes, not a string
        clientsocket.send(send_bytes)
        clientsocket.close()

except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()