try:
    a = int(input())
    b = int(input())
    c = a/b
    print(c)
except ZeroDivisionError:
    print('zero division error')
except ValueError: #multiple except blocks can be used
    print('value error')
except NameError:
    print('name error')