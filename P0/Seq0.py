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