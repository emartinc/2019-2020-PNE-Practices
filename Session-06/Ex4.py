import termcolor

class Seq:

    def __init__(self, strbases):
        self.strbases = strbases

        valid_bases = ["A", "C", "G", "T"]
        for element in strbases: #this is to check that the string used for initialization only contains valid bases
            if element not in valid_bases:
                print("ERROR!")
                self.strbases= "ERROR"
                return

        self.strbases= strbases
        print("A new sequence has been created!")

    def __str__(self):
        return self.strbases #to just return the string with the valid sequence

    def len(self): #to measure the length of the inserted sequences
        return(len(self.strbases))

def print_seqs(sequences, color): #in order to print a list of sequences
    for seqs in sequences:
        termcolor.cprint(f"Sequence: {sequences.index(seqs)} Length: {seqs.len()}{seqs}", color)

def generate_seqs(pattern, number): #Generate a list of sequences in which the give patter is repeated from 1 to number and it returns a list with all the sequences.
    seqs = []
    for i in range(1, number + 1):
        seqs.append(Seq(pattern * i))
    return seqs


#main program
seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

termcolor.cprint("List 1:", 'blue')
print_seqs(seq_list1, 'blue')

print()
termcolor.cprint("List 2:", 'green')
print_seqs(seq_list2, 'green')