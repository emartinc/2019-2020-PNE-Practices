#Ex. 3
def fibon(n): #here we are difining a function

#For the term 0 and 1 no calculation is requiered

    if n in [0, 1]:
        return n

    n1 = 0
    n2 = 1

#parcial result

    term_n = 0 #to store the result

#calculate the nth term

    for i in range(2, n+1):
        term_n = n1 + n2

#update the previous terms
        n1 = n2
        n2 = term_n

    return term_n

#here we define another function

def fibosum(n):

#Partial sum

    res = 0 #to store a value
    for i in range(n+1):
        res += fibon(i)
    return res


print("Sum of the First 5 terms of the Fibonacci series: ", fibosum(5))
print("Sum of the First 10 terms of the Fibonaci series: ", fibosum(10))