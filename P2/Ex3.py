from client0 import Client

print("Practice 2, Exercise 3")

#Parameters of the server to talk to
IP = "192.168.0.29"
PORT = 8080

#Create a client object
c = Client(IP, PORT)

#Send a message to the server
print("Sending a message to the server...")
response = c.talk("Testing!")
print(f"Response: {response}")