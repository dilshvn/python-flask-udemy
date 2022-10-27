def decor(func): #decorator func
    def inner(x, y):
        print(x, y)
        if y == 0:
            print('division by zero')
            return #returns 'None'
        func(x, y)
    return inner

@decor #decorated
def divide(a, b): #func
    return a/b

print(divide(20, 3))
"""
o/p:
20 3 #decoration
6.666666666666667 #func output
"""
print(divide(10, 0))
"""
o/p:
division by zero #decoration
None #func output
"""