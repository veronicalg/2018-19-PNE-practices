#Client code for practice 3:

import socket

# SERVER IP, PORT
IP = "127.0.0.1"
PORT = 8082



while True:

    sentence = "" # The message we are going to send
    msg = input('>') # Le ponemos el prompt.

    while len(msg)>0:
        sentence = sentence + msg + '\n'  # Le enviamos una cadena.
        msg = input('')

    if len(sentence)==0:
        sentence = '\n'


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # Send the request message to the server
    s.send(str.encode(sentence))

    # Receive the servers respoinse
    response = s.recv(2048).decode()

    # Print the server's response
    print("Response: {}".format(response))

    s.close()