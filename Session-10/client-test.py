from client0 import Client

# Parameters of the server to talk to
PORT = 8080
IP = "192.168.0.29"

# Repeat five times
for i in range(5):

    # Create a client object
    client = Client(IP, PORT)

    # Send a message to the server
    client.debug_talk(f"Message {i}")