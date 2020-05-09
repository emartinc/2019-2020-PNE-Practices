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

def print_seqs(sequences): #in order to print a list of sequences
    for seqs in sequences:
        print("Sequence:", sequences.index(seqs), "Length:",seqs.len(),seqs)


#main program
seq_list = [Seq("AGG"), Seq("CAAT"), Seq("GATACA")] #creating a list of the sequences

print_seqs(seq_list)