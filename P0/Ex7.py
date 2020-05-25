from Seq0 import *

FOLDER = "../Session-04/"
GENES = "U5.txt"
BASES = ['A', 'C', 'T', 'G']


Dna_file= (FOLDER + GENES)
seq = seq_read_fasta(Dna_file)
seq20 = seq[:20]
comp = seq_complement(seq20)

print("Exercise 7")
print("Gene U5:")
print("Fragment:", seq20)
print("Complementary:", comp)