from client0 import Client
from Seq1 import Seq


print("Practice 2 , Exercise 6")

#Parameters
IP = "192.168.0.29"
PORT = 8080
FOLDER = "../Session-04/"
filename = FOLDER + 'FRAT1.txt'

# Create sequence
s = Seq()

# Read the file
s.read_fasta(filename)

# Creating fragments of length 10
fragment1 = "Fragment 1: "
fragment2 = "Fragment 2: "
fragment3 = "Fragment 3: "
fragment4 = "Fragment 4: "
fragment5 = "Fragment 5: "
fragments = [fragment1, fragment2, fragment3, fragment4, fragment5]

i = 0
f = 0
while f < len(fragments):
    sequence = str(s)
    fragments[f] += sequence[i]
    i += 1
    if i % 10 == 0:
        f += 1

#connect
c = Client(IP, PORT)

c.talk(fragments[0])
c.talk(fragments[1])
c.talk(fragments[2])
c.talk(fragments[3])
c.talk(fragments[4])

#Print

print("Gene FRAT1:", s)
for frag in fragments:
    print(frag)