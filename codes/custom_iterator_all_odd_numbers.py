#infinite custom iterator
class Infinite_Iter:

    def __iter__(self): #constructor __init__ is optional
        self.num = 1
        return self.num
    
    def __next__(self):
        num = self.num
        self.num += 2
        return num

i = Infinite_Iter()
a = iter(i)
print(next(a)) #1
print(next(a)) #3
print(a.__next__()) #5
print(a.__next__()) #7


