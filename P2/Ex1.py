from client0 import Client

print("Practice 2, Exercise 1")

#Parameters of the server to talk to
IP = "192.168.0.29"
PORT = 8080

#Create a client object
c = Client(IP, PORT)

#Test the ping method
c.ping()

#Print the IP and PORTs
print(f"IP: {c.ip}, {c.port}")
