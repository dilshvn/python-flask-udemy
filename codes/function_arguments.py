def hello(name, msg = ', how are you?'): #func with default parameter
    print('Hello ' + name + msg)

hello('Dilshan') #Hello Dilshan, how are you?
hello('Dilshan', ', what\'s up?') #Hello Dilshan, what's up? -> default 'msg' var is reassigned

def sumAll(*args): #takes multi arguments
    sum = 0
    for i in args:
        sum += i
    return sum

print(sumAll(1, 2, 3, 4, 5)) #15

def Arg(a, b, c):
    print(a, b, c)

Arg(b = 2, c = 3, a = 1) #1 2 3
