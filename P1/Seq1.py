from pathlib import Path

def seq_ping():
    print("OK!")


def seq_read_fasta(filename):
    "Read a file with a DNA sequence in FASTA format the parameter is the filename (String) and it returns the sequence(String)"

    #Read the file
    contents = Path(filename).read_text()

    #Remove the head
    body = contents.split('\n')[1:]

    #Return the body as a string without the \n characters
    return "".join(body)


def seq_len(seq):
    return len(seq)


def seq_count_base(seq, base):
    "Counting the given base on the sequence parameter the sequence (String) parameter base(Character) returns the times that the inserted base appears in the sequence (Integer)"
    return seq.count(base)


def seq_count(seq):
    "Calculate the number of bases in the sequence parameter sequence (String) returns a Dictionary with the results"
    res = {'A': seq_count_base(seq, 'A'), 'T': seq_count_base(seq, 'T'),
           'C': seq_count_base(seq, 'C'), 'G': seq_count_base(seq, 'G')} #defining the dictionary
    return res



def seq_reverse(seq):
    "Return the reverse sequence parameter sequence (String) returns a the sequence reversed (String)"
    return seq[::-1]


def seq_complement(seq):
    "Returns the complementary sequence parameter sequence (String) returns the comp. sequence (String)"

    #Creating a dictionary of complementary bases
    basec = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    res = ""

    for b in seq:
        res += basec[b]

    return res

def valid_seq(strbases):
    validbases = ["A","C","G","T"]
    for element in validbases:
        if element not in validbases:
            return False
    return True

class Seq:

    #Identification string for the Null and Invalid sequences
    NULL = "NULL"
    ERROR = "ERROR"

    def __init__(self, strbases=NULL):
        """Constructor:
        :type strbases: string with the bases of the sequence
        """

        # -- Check if it is the null seq
        if strbases == self.NULL:
            self.strbases = self.NULL
            print("NULL Seq created")
            return

        # -- Check if the string passed by the user is valid
        if not self.valid_str(strbases):
            self.strbases = self.ERROR
            print("INVALID Seq!")
            return

        # -- Store the string in the object
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        return self.strbases #to just return the string with the valid sequence

    def len(self): #to measure the length of the inserted sequences
        return(len(self.strbases))

    def valid_str(strbases):
        """Check if the string is valid or not"""

        # -- Valid bases
        valid_bases = ['A', 'C', 'T', 'G']

        for b in strbases:

            # -- IF one base is not valid...
            if b not in valid_bases:
                return False

        # -- All the bases are valid --> the string is valid
        return True


def print_seqs(sequences): #in order to print a list of sequences
    for seqs in sequences:
       print(f"Sequence: {sequences.index(seqs)} Length: {seqs.len()}{seqs}")

def generate_seqs(pattern, number): #Generate a list of sequences in which the give patter is repeated from 1 to number and it returns a list with all the sequences.
    seqs = []
    for i in range(1, number + 1):
        seqs.append(Seq(pattern * i))
    return seqs
