#PROPERTY AS A DECORATOR

class Celsius:
    def __init__(self, temp = 0): #constructor
        self._temp = temp

    def conv_to_fahrenheit(self):
        return (self._temp*1.8) + 32

    @property #getter method, as a decorator
    def temp(self): #not using get_temp
        print('getting value')
        return self._temp

    @temp.setter #setter method, as a decorator
    def temp(self, value): #not using set_temp
        if value < -273:
            raise ValueError('temp below -273: impossible')
        print('setting value')
        self._temp = value

c = Celsius(5)
print(c.temp)
"""
o/p:
getting value
5
"""
c.temp = 100
print(c.temp)
"""
o/p:
setting value
getting value
100
"""