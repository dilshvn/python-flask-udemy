def outer():
    a = 5
    def inner():
        nonlocal a
        #a isn't a local variable to inner func
        a = 10
        print("inner: ", a)
    inner()
    print("outer: ", a)

outer()
#inner and outer: both 10