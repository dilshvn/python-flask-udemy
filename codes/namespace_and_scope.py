#name -> identifier
#id -> address in RAM

a = b = 2
print(id(a) == id(b) == id(2)) #True

a = 3
print(id(a) == id(b)) #False
print(id(a) == id(3)) #True

#scope
def outer_func():
    global a #global variables can be accessed from anywhere
    a = 20

    def inner_func():
        global a #refering to the same 'a' we used earlier
        a = 30
    
    inner_func()
    print(a)

outer_func() #30

