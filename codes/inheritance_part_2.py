#inheritance
class Bird:
    def __init__(self):
        print('bird constructor')
    
    def whatType(self):
        print('bird')
    
    def canSwim(self):
        print('can swim')

class Parrot:
    species = 'bird' #class attribute

    def __init__(self, name, age): #instance attribute -> constructor
        print('parrot constructor')
        self.name = name
        self.age = age

    def canSing(self, song):
        return self.name, song #returns tuple

class Penguin(Bird): #inherits from Bird class, properties in Bird class will be inherited

    def __init__(self):
        super().__init__() #calls Bird's constructor
        print('penguin constructor')

    def whoIsThis(self):
        print('penguin')
    
    def canRun(self):
        print('can run')

#instantiating Parrot class
parrot1 = Parrot('polly', 2) #parrot constructor
parrot2 = Parrot('toby', 3) #parrot constructor

#accessing class attributes
print(parrot1.species) #bird
print(parrot2.__class__.species) #bird -> similar method to above line (without __class__)

print(parrot1.name, parrot1.age) #polly 2
print(parrot2.name, parrot2.age) #toby 3
print(parrot1.canSing('despacito')) #('polly', 'despacito')

penguin1 = Penguin() #runs Bird's constructor
"""
bird constructor
penguin constructor
"""
penguin1.whoIsThis() #from Penguin class (subclass) -> penguin
penguin1.canSwim() #from Bird class (base class) -> can swim
penguin1.canRun() #from Penguin class (subclass) -> can run