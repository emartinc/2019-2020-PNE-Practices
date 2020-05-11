from client0 import Client

print("Practice 3, Exercise CLIENT SERVER")

# Parameters for the server
IP = "127.0.0.1"
PORT = 8080

# Creating a client object
c = Client(IP, PORT)
sequence = "GATGGATGGAGAGGATAGATAGAGATAGATAGAGAG"

print("Connection to SERVER at", IP, ", PORT: ", PORT)

# TEST PING
print("* Testing PING...")
print(c.talk("PING"))

# TEST GET
print("* Testing GET...")
print("GET 0:", c.talk("GET 0"))
print("GET 1:", c.talk("GET 1"))
print("GET 2:", c.talk("GET 2"))
print("GET 3:", c.talk("GET 3"))
print("GET 4:", c.talk("GET 4"))

# TEST INFO
print("* Testing INFO...")
print(c.talk("INFO " + sequence))

# TEST COMP
print("* Testing COMP...")
print("COMP " + sequence)
print(c.talk("COMP " + sequence))

# TEST REV
print("* Testing REV...")
print("REV " + sequence)
print(c.talk("REV " + sequence))

# TEST REV
print("* Testing GENE...")
files_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
for file in files_list:
    print("GENE", file)
    print(c.talk("GENE " + file))