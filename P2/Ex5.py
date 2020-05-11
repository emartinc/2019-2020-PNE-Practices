from client0 import Client
from Seq1 import Seq

print("Practice 2, Exercise 5")

#Parameters
IP = "192.168.0.29"
PORT = 8080
FOLDER = "../session-04/"
filename = FOLDER + 'U5.txt'
s = Seq()
s.seq_read_fasta(filename)

#Create a client object
c = Client(IP, PORT)

c.debug_talk("Sending the U5 Gene to the server..")
c.debug_talk(s)
