import socket

# SERVER IP, PORT
PORT = 8081
IP = "192.168.0.29"

while True:
    #Asking the user for the message
    message = input("Type your message: ")

    #Creating the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Establishing the connection to the Server
    s.connect((IP, PORT))

    #Sending the user message
    s.send(str.encode(str(message)))

    #Closing the socket
    s.close()