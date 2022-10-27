#iter, next methods

list1 = [11, 22, 33, 44]
iter1 = iter(list1)
print(iter) #returns nothing
print(next(iter1)) #11
print(next(iter1)) #22
#.__next__() is same as next()
print(iter1.__next__()) #33
print(iter1.__next__()) #44
print(iter1.__next__()) #StopIteration error