from client0 import Client

print("Practice 2, Exercise 2")

#Parameters of the server to talk to
IP = "192.168.0.29"
PORT = 8080

#Create a client object
c = Client(IP, PORT)

#Print the IP and PORTs
print(c)