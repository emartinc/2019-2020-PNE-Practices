from Seq0 import *

FOLDER = "../Session-04/"
txt = ".txt"
GENES = ["U5", "ADA", "FRAT1", "FXN",]
BASES = ['A', 'C', 'T', 'G']

print(f"Exercise 4")


for gene in GENES:
    seq = seq_read_fasta(FOLDER + gene + txt)
    print()
    print(f"Gene:", gene)
    for base in BASES:
        counter = seq_count_base(seq, base)
        print(base, counter)
