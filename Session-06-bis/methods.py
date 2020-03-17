## the methods are the actions that the objects in the class can perform.
# the first method that we are going to implement is the initialization method,
# this method is a special method that is called every time a new object is created.

class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):  # all the methods have the special parameter self as the first parameter
        self.strbases = strbases  #initialize the sequence with the value, passed as an argument when creating the object

        print("New sequence created!!")


# main program
## we create an object of the class seq, we store data inside them, this data will be called strbases
s1 = Seq("AGTACACTGGT")
s2 = Seq("CGTAAC")


## when we run the progam.
# When the s1 object is created, the string "New sequence created!" is printed.
# The same happens when the s2 object is also created.
