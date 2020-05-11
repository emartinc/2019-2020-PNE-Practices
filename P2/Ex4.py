from client0 import Client

print("Practice 2, Exercise 4")

#Parameters of the server to talk to
IP = "192.168.0.29"
PORT = 8080

#Create a client object
c = Client(IP, PORT)

c.debug_talk("Message 1---")
c.debug_talk("Message 2: Testing !!!")