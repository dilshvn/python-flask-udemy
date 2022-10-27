#PROPERTY

#built-in func, useful in oop -> creates & returns a property object
#property(fget = None, fset = None, fdel = None, doc = None)
#property object has 3 methods -> setter(), getter(), delete()
#temp = property(get_temp, set_temp)

class Celsius:
    def __init__(self, temp = 0): #constructor
        print('assigning temp value')
        self._temp = temp #private attribute
    
    def convert_to_fahrenheit(self):
        return(self._tem*1.8) + 32
    
    def get_temp(self): #getter func
        print('getting temp value')
        return self._temp
    
    def set_temp(self, value): #setter func
        if value < -273:
            raise ValueError('temp below -273: impossible')
        print('setting temp value')
        self._temp = value
    
    temp = property() #making empty property
    temp = temp.getter(get_temp) #assign fget
    temp = temp.setter(set_temp) #assign fset

c = Celsius(5)
print(c.temp)
"""
o/p:
assigning temp value
getting temp value
5
"""
c.temp = 100
print(c.temp)
"""
o/p:
setting temp value
getting temp value
100
"""
c1 = Celsius(-300)
print(c1.temp) #-300 -> instatiating value has no problem here
c1.temp = c1.temp #ValueError: temp below -273: impossible -> using c1.temp = -300 will throw the same err