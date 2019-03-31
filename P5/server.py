#--Web server that redirects you to html pages depending on the resource using http module

import http.server
import socketserver
import termcolor

# Define the Server's port
PORT = 8009


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happy server: It always returns a message saying
        # that everything is ok

        # Message to send back to the client, depending on the resource
        if self.path == "/":
            with open ("indexx.html", "r") as f:
                contents = f.read()
        elif self.path == "/blue":
            with open ("blue.html", "r") as f:
                contents = f.read()
        elif self.path == "/pink":
            with open("pink.html", "r") as f:
                contents = f.read()
        else:
            with open("error.html", "r") as f:
                contents = f.read()


        # Generating the response message
        self.send_response(200)  # -- Status line: OK! #El navegador va a ser contestado.

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html') #Código en formato html.
        self.send_header('Content-Length', len(str.encode(contents))) #Conocer numero de bytes codificados.

        # The header is finished
        self.end_headers() #3

        # Send the response message
        self.wfile.write(str.encode(contents)) #--Enviar el contenido.

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()

print("")
print("Server Stopped")