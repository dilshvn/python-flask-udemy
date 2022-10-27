def decor(func): #decorator
    def inner(): #inner func
        print('top decoration') #decoration
        func() #calling arg
        print('bottom decoration')
    return inner #output has to be called later

def simple(): #func
    print('i\'m a simple func')

decor1 = decor(simple) #returns inner
decor1() #inner is called here
"""
o/p:
top decoration
i'm a simple func
bottom decoration
"""

#there's another way to decorate
@decor #use the decorator func name with @
def simplefunc(): #func
    print('i\'m also a simple func')

#now, whenever simplefunc() is called -> decor() is also called automatically
simplefunc()
"""
o/p:
top decoration
i'm a simple func
bottom decoration
"""