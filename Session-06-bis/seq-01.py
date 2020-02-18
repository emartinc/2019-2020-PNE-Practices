class Seq:
    """A class for representing sequence objects"""
    def __init__(self, strbases):
        self.strbases = strbases
        print("New sequence created")

    def __str__(self):
        return self.strbases
    def len(self):
        return len(self.strbases)
class Gene(Seq):
    def _init_(self):
     pass #there is nothing inside this class



# Main program
s1 = Seq("AACGT")
s2 = Seq("CCGTGCA")
g = Gene("ACCTGA")

print(f"Sequence 1:{s1}")
print(f"Sequence 2:{s2}")
print(f"Gene:{g}")

l1 = s1.len()

print(f"The length of the sequence1 is {l1}")
print(f"The length of the sequence 2 is {s2.len()}")
print(f"The length of the gene is {g.len()}")

print("Testing objects...")