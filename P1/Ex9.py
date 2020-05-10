from Seq1 import Seq

FOLDER ="../session-04/"
txt= ".txt"
GENES ="U5"
FILENAME = FOLDER + GENES + txt
print("Practice 1, Exercise 9")

s = Seq()

s.seq_read_fasta(FILENAME)

print(f"Sequence : (Length: {s.len()}) {s}")
print(f"  Bases: {s.count()}")
print(f"  Rev:   {s.reverse()}")
print(f"  Comp:  {s.seq_complement()}")