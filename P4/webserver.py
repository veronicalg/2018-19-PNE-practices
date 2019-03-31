#--Web server to give the user access to three different pages in HTML.

import socket
import termcolor

IP = "127.0.0.1"
PORT = 8081
MAX_OPEN_REQUESTS = 5


def process_client(cs):
    """Process the client request.
    Parameters:  cs: socket for communicating with the client"""

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")

    separar_msg = msg.split(" ") #It splits the message through the blank spaces.
    print(separar_msg)  #--It creates a list with the elements separated by the blank spaces.
    resource = separar_msg[1] #--We keep the first element of our list, which is the resource.
    print("Resource", resource)
    if resource == "/":
        filename = "indexx.html"
    elif resource == "/pink":
        filename = "pink.html"
    elif resource == "/blue":
        filename = "blue.html"
    else:
        filename = "error.html"



    # Print the received message, for debugging
    print()
    print("Request message: ")
    termcolor.cprint(msg, 'green')

    # Build the HTTP response message. It has the following lines
    # Status line
    # header
    # blank line
    # Body (content to send)

    # This new contents are written in HTML language
    with open(filename, "r") as f:
        contents = f.read()

    # -- Everything is OK
    status_line = "HTTP/1.1 200 OK\r\n"

    # -- Build the header
    header = "Content-Type: text/html\r\n"
    header += "Content-Length: {}\r\n".format(len(str.encode(contents)))

    # -- Build the message by joining together all the parts
    response_msg = str.encode(status_line + header + "\r\n" + contents)
    cs.send(response_msg)

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