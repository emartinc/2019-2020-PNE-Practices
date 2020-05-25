from Seq1 import Seq  # We import the functions from Seq0.py

print("Practice 1, Exercise 10")

FOLDER = "../Session-04/"  # Obtaining the gene files from this folder
bases = ["A", "C", "T", "G"]
GENES= ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]  # List of genes

for gene in GENES:  # We go throw every file in the list , U5 , ADA...
    sequence = Seq() #here we are creating the seq ogbject, an empty object
    sequence.read_fasta(FOLDER + gene + ".txt")
    # This function reads a file and return it's content
    # Add the folder and .txt to read properly the file
    dict_bases = sequence.count()
    # seq_count()
    # This function counts the number of bases in a sequence in a dictionary
    min_value = 0  # Set a min value
    best_base = ""
    for base, value in dict_bases.items():
        # .items() gets the keys and values from a dictionary
        while value > min_value:  # With this loop , find the most frecuent base
            min_value = value
            best_base = base
            # Replace the minimun value with the "new minimun value" and the base with this value is set as best_base

    print("Gene", gene, " : Most frequent Base: ", best_base)