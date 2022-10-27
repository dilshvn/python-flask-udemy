#SHORT WAY OF DOING THE SAME THING

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
    
    temp = property(get_temp, set_temp) #property -> without creating empty property first, shorter method

c = Celsius(5)
print(c.temp)
"""
o/p:
assigning temp value
getting temp value
5 -> prints same result
"""
print(c.__dict__) #{'_temp': 5} -> shows all instance variables (has only 1 in this case)
print(c.__dict__['_temp']) #5 -> prints only the values we need
