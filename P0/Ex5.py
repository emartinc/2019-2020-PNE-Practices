from Seq0 import *

FOLDER = "../session-04/"

GENES = ["U5.txt", "ADA.txt", "FRAT1.txt", "FXN.txt"]
BASES = ['A', 'C', 'T', 'G']

print(f"Exercise 5")

for gene in GENES:
    seq = seq_read_fasta(FOLDER + gene)
    print(f"Gene {gene}: {seq_count(seq)}")