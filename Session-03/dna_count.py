#Introduce the sequence
seq = input("Introduce the sequence: ")

#bases counters
a = 0
t = 0
c = 0
g = 0

for b in seq:
    if b == 'A':
        a += 1
    elif b == 'T':
        t += 1
    elif b == 'C':
        c += 1
    elif b == 'G':
        g += 1

total_length = a + t + c + g

#Printing the results:
print("Total length:", total_length)
print("A:" , a)
print("C:" , c)
print("T:" , t)
print("G:" , g)