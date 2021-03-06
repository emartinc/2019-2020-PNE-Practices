import socket
import termcolor

class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = int(port)

    def ping(self):
        print("OK!")

    def __str__(self):
        return "Connection to SERVER at " + self.ip + " , PORT: " + str(self.port)

    def talk(self, msg): #Send the string (message) to the app running in the given IP and Port
        # Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))
        # Send data.
        s.send(str.encode(str(msg)))
        # Receive data
        response_raw = s.recv(2048)
        response = response_raw.decode()
        # Close the socket
        s.close()
        # Return the response
        return response

    def debug_talk(self, msg):
        message = str(msg)
        response = self.talk(msg)
        print("To Server: ", end="")
        termcolor.cprint(message, 'green')
        print("From Server: ", end="")
        termcolor.cprint(response, 'blue')
