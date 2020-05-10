from Seq1 import Seq

print("Practice 1, Exercise 5")

s1 = Seq()
s2 = Seq("GATCGG")
s3 = Seq("Invalid sequence")

validbases = ["A", "T", "G", "C"]
print("Sequence 1: (Length : ", s1.len(), ")", s1)
for element in validbases:
    print(element + ":", s1.count_base(element), end=",  ")
print("\nSequence 2: (Length : ", s2.len(), ")", s2)
for element in validbases:
    print(element + ":", s2.count_base(element), end=",  ")
print("\nSequence 3: (Length : ", s3.len(), ")", s3)
for element in validbases:
    print(element + ":", s3.count_base(element), end=",  ")