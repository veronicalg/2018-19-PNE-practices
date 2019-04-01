#Server code for P3

import socket
import termcolor
from Seq import Seq

# Configure the Server's IP and PORT
PORT = 8082
IP = "127.0.0.1"
MAX_OPEN_REQUESTS = 5

def validSequence(s):
    valid = "ACTG"
    for letter in s:
        if letter not in valid:
            return False
    return True


def calculations (s1, command):
    print("Treating", command)
    if command == "len":
        return s1.len()
    elif command== "complement":
        return s1.complement()
    elif command == "reverse":
        return s1.reverse()
    elif command == "countA":
        return s1.count("A")
    elif command == "countT":
        return s1.count("T")
    elif command == "countG":
        return s1.count("G")
    elif command == "countC":
        return s1.count("C")
    elif command == "percA":
        return s1.perc("A")
    elif command == "percT":
        return s1.perc("T")
    elif command == "percG":
        return s1.perc("G")
    elif command == "percC":
        return s1.perc("C")
    else:
        return "ERROR"


def process_client(cs):
    """Process the client request.
    Parameters:  cs: socket for communicating with the client"""

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")

    # Printing the message in yellow color.
    termcolor.cprint(msg, 'red')

    # Server finishes if EXIT is received.
    #if msg == "EXIT":
        #sys.exit(0)

    response = ""
    if msg == '\n':
        response = 'ALIVE'

    else:
        sentence = msg.split('\n')
        print(sentence) # List with all the inputs from the client
        print("Valuing", sentence[0])
        if (validSequence(sentence[0])):
            response = 'OK\n'


            s1 = Seq(sentence[0])


            # Recorremos comandos
            for i in range(1, len(sentence)-1):
                print("Calculating", i, sentence[i])
                r = calculations(s1, sentence[i])
                print ("Output", r)
                response = response + str(r) + '\n'

        else:
            response = 'ERROR'


    # Print the received message, for debugging
    print("Request message: {}".format(response))

    # Send the msg back to the client (echo)
    cs.send(str.encode(response))

    # Close the socket
    cs.close()


# MAIN PROGRAM

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and PORT
serversocket.bind((IP, PORT))

# Configure the server sockets
# MAX_OPEN_REQUESTS connect requests before refusing outside connections
serversocket.listen(MAX_OPEN_REQUESTS)

print("Socket ready: {}".format(serversocket))

while True:
    # accept connections from outside
    # The server is waiting for connections
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    # Service the client

    process_client(clientsocket)