#custom iterator
class Powers_of_Two:
    '''class to implement iterator of powers of 2''' #this is called docstring or block comment
    def __init__(self, max = 0): #__init__ is a constructor
        self.max = max #self.max is an instance
    
    def __iter__(self): #__iter__ is a method
        self.n = 0 #self.n is an instance
        return self

    def __next__(self): #__next__ is a method
        if self.n <= self.max:
            result = 2**self.n
            self.n += 1
            return result
        else:
            raise StopIteration

print(Powers_of_Two.__doc__) #prints docstring
a = Powers_of_Two(4) #4 is assigned to max
print(a) #returns nothing
i = iter(a)
print(next(i)) #1 -> 0th power of 2
print(next(i)) #2 -> 1st power of 2
print(next(i)) #4
print(next(i)) #8
print(i.__next__()) #16 -> similar to next(i)
