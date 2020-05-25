from pathlib import Path
class Seq:
    """A class for representing sequence objects"""
    NULL = "NULL"
    ERROR = "ERROR"

    def __init__(self, strbases = "NULL" ):
        if strbases == self.NULL:
            self.strbases = self.NULL
            print("NULL Seq created")
            return

        if not self.valid_str(strbases):
            self.strbases = self.ERROR
            print("INVALID Seq!")
            return

        self.strbases = strbases
        print("New sequence created")

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)

    @staticmethod #this is a function defined inside a class
    def valid_str(strbases):
        valid_bases = ['A', 'C', 'T', 'G']
        for element in strbases:
            if element not in valid_bases:
                return False
        return True

    def len(self):
        if self.strbases in [self.NULL, self.ERROR]:
            return 0
        else:
            return len(self.strbases)

    def count_base(self, base):
        return self.strbases.count(base)

    def count(self):
        basesdict = ["A", "C", "T", "G"]
        counter= []
        for element in basesdict:
            counter.append(self.count_base(element))
        dictionary = dict(zip(basesdict, counter))
        return dictionary

    def reverse(self):
        if self.strbases in [self.NULL, self.ERROR]: #to check if its an invalid seq or null
            return self.strbases
        else:
            return self.strbases[::-1] #in order to reverse the valid given seq.

    def complement(self):
        if self.strbases in [self.NULL, self.ERROR]: #to check if its an invalid seq or null
            return self.strbases
        # Creating a dictionary of complementary bases
        else:
            bases = ["A", "C", "T", "G"]
            compbases = ["T", "G", "A", "C"]
            dictcompbases = dict(zip(bases, compbases))
            complementary = ""
            for i in self.strbases:
                for base, cobases in dictcompbases.items():
                    if i == base:
                        complementary += cobases
            return complementary

    def read_fasta(self, filename):
        "Read a file with a DNA sequence in FASTA format the parameter is the filename (String) and it returns the sequence(String)"
        # Read the file
        contents = Path(filename).read_text()
        # Remove the head
        body = contents.split('\n')[1:]
        # Return the body as a string without the \n characters
        self.strbases = "".join(body)
        return self