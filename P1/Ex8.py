from Seq1 import Seq

print("Practice 1, exercise 7")

s1 = Seq()
s2 = Seq("GATCCTAGGACGTA")
s3 = Seq("Invalid seq")

print(f"Sequence 1: length {s1.len()} {s1}")
print(f"Bases:{s1.count()}")
print(f"Reverse:{s1.reverse()}")
print(f"Complementary:{s1.complement()}")

print(f"Sequence 2: length {s2.len()} {s2}")
print(f"Bases:{s2.count()}")
print(f"Reverse:{s2.reverse()}")
print(f"Complementary:{s2.complement()}")

print(f"Sequence 3: length {s3.len()} {s3}")
print(f"Bases:{s3.count()}")
print(f"Reverse:{s3.reverse()}")
print(f"Complementary:{s3.complement()}")