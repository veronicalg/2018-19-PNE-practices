#Echo server for exercise 2.


import http.server
import socketserver
import termcolor

# Define the Server's port
PORT = 8001


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')


        if self.path=="/":
            f = open("form3.html", 'r')
            contents = f.read()

        elif self.path[0:5] == "/echo" and "chk=on" in self.path:
            msgA= self.path.split('=')[1]
            msgB = msgA.split('&')[0]
            contents = """<html><body>
            MESSAGE RECEIVED: """ + msgB.upper() + """
            <p><a href="http://127.0.0.1:8001/">MAIN PAGE</a></p>
            </body></html>"""

        elif self.path[0:5] == "/echo":
            msgA = self.path.split('=')[1]
            msgB = msgA.split('&')[0]
            contents = """<html><body>
                        MESSAGE RECEIVED: """ + msgB + """
                        <p><a href="http://127.0.0.1:8001/">MAIN PAGE</a></p>
                        </body></html>"""

        else:
            f = open("errorfile.html", "r")
            contents = f.read() #Crear archivo error con el link de la pagina principal href

            pass        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

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
