from client0 import Client
from Seq1 import Seq

print("Practice 2, Exercise 7")

# -- Parameters server 1
IP = "192.168.0.29"
PORT1 = 8081
PORT2 = 8080
FOLDER = "../Session-04/"
filename = FOLDER + 'FRAT1.txt'

s = Seq()
s.read_fasta(filename)

#Creating the fragments
fragment1 = "Fragment 1: "
fragment2 = "Fragment 2: "
fragment3 = "Fragment 3: "
fragment4 = "Fragment 4: "
fragment5 = "Fragment 5: "
fragment6 = "Fragment 6: "
fragment7 = "Fragment 7: "
fragment8 = "Fragment 8: "
fragment9 = "Fragment 9: "
fragment10 = "Fragment 10: "
fragments = [fragment1, fragment2, fragment3, fragment4, fragment5, fragment6,
             fragment7, fragment8, fragment9, fragment10]

i = 0
f = 0
while f < len(fragments):
    sequence = str(s)
    fragments[f] += sequence[i]
    i += 1
    if i % 10 == 0:
        f += 1

#connecting
c1 = Client(IP, PORT1)
c2 = Client(IP, PORT2)

r = 0
while r < len(fragments):
    if r % 2 == 0 or r == 0:
        c1.talk(fragments[r])
    else:
        c2.talk(fragments[r])

    r += 1

#print

print("Gene FRAT1:", s)
for frag in fragments:
    print(frag)