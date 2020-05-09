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

#main program
s1 = Seq("AGTACACTGGT")
s2 = Seq("Hello? Am I a valid sequence?")

print(f"Sequence 1:", s1)
print(f"Sequence 2:", s2)