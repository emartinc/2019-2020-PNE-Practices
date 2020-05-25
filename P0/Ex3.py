from Seq0 import *

FOLDER = "../Session-04/"
txt = ".txt"
GENES = ["U5","ADA", "FRAT1", "FXN"]

print("Exercise 3")
for gene in GENES:
    seq = seq_read_fasta(FOLDER + gene + txt)
    length = seq_len(seq)
    print(f"Gene:", gene, "Length:",length)