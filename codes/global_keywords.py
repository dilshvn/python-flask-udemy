def func1():
    x = 1 #local

    def func2():
        global x 
        x = 2
        return x

    print(x) #1 
    print(func2()) #2 -> prints global x
    print(x) #1 -> local var isn't affected by global x

func1()
print(x) #2 -> affected by global x
    
    