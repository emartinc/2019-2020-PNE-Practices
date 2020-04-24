from Seq0 import *

PRACTICE = 8
FOLDER = "../Session-04/"
EXT = ".txt"
GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
BASES = ['A', 'T', 'C', 'G']

print(f"-----| Exercise {PRACTICE} |------")

for gene in GENES:
    seq = seq_read_fasta(FOLDER + gene + EXT)

    # with this we create a dictionary with the values
    d = seq_count(seq)

    # with this we create a list with all the values
    ll = list(d.values())

    # with this we calculate the maximum
    m = max(ll)

    #with this we print the base
    print(f"Gene {gene}: Most frequent Base: {BASES[ll.index(m)]}")