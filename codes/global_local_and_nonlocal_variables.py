#global variables can be accessed from anywhere

def func():
    global x #global -> outside local
    x = 'after'
    return x 

x = 'before'
print(x) #before
print(func()) #after

#nonlocals variables are used in nested functions

def outer():
    x = 1 #local -> will be affected by nonlocal x

    def inner():
        nonlocal x #nonlocal
        x = 2
        print(x)
    
    inner() #2
    print(x) #2

x = 3 #won't be affected by local or nonlocal
outer()
print(x) #3
