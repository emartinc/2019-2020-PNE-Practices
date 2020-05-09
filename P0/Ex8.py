from Seq0 import *

FOLDER = "../session-04/"
txt =".txt"
GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
BASES = ['A', 'T', 'C', 'G']

print(f"Exercise 8")

for gene in GENES: #for each element on the list GENE
    seq = seq_read_fasta(FOLDER + gene + txt)

    #Creating a dictionary with the values
    d = seq_count(seq) # function to Calculate the number of bases in the sequence parameter sequence (String) returns a Dictionary with the results

    #Creating a list with all the values
    list_values= list(d.values())

    #Calculate the maximum
    m = max(list_values)

    #Print the base
    print(f"Gene:", gene)
    print("Most frequent Base:", BASES[list_values.index(m)])  # the .index(m) is to indicate the base associated with the maximum number