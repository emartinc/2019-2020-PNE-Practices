from Seq0 import *
#first we create the program to print the sequence of the 20 first bases
FOLDER = "../session-04/"
FILENAME = "U5.txt"

DNA_FILE =(FOLDER + FILENAME)

#Open the DNA file
seq = seq_read_fasta(DNA_FILE)
seq20 = seq[:20]
reverse = seq_reverse(seq20)
print("Exercise 6")
print(f"Gene U5:")

print(f"Fragment:",seq20)
print(f"Reversed:",reverse)

