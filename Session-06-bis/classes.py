
##a class is a template we use for creating objects.
# Inside the class we define all the methods of the objects of that class, and we program their behaviour.

##first, we start defining an empty class

class Seq:
    """A class for represening sequences"""
    pass

##once the class is defined we can create objects of this class (in this case class Seq):
s1 = Seq()  #we have placed a break point here, Breakpoints are source code markers that let you suspend program execution at a specific point and examine its behavior.
s2 = Seq()

print("Testing...")

#press the debug option and then the step over function twice, then two new empty objects have been created