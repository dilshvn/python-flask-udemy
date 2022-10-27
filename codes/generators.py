def gen():
    n = 1
    print('first')
    yield n #generator functions have 'yield' statements, 'return' only returns once
    
    n += 1
    print('second')
    yield n

    n += 1
    print('last')
    yield n

gen1 = gen()
#next is used to iterate
next(gen1) #first
next(gen1) #second
next(gen1) #last
next(gen1) #error