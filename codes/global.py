var = 0

def read():
    print(var)

def write1():
    global var
    var = 1
#here, var is a global variable

def write2():
    var = 2
#here, var is a local variable

read()

write1()
read()

write2()
read()