#inheritance
#base class is also called superclass

class Bird:

    def __init__(self):
        print('bird class constructing')
    
    def whatType(self):
        print('bird')
    
    def canSwim(self):
        print('can swim')

class Penguin(Bird): #Penguin subclass inherits from Bird superclass

    def __init__(self):
        super().__init__() #calls superclass constructor
        print('penguin class constructing')

    def whoIsThis(self):
        print('penguin')

    def canRun(self):
        print('can run')

peng1 = Penguin()
'''
o/p:
bird class constructing #superclass constructor is called in subclass constructor
penguin class constructing #from subclass constructor
'''
peng1.whatType() #bird -> from superclass
peng1.whoIsThis() #penguin -> from subclass
peng1.canSwim() #can swim -> from superclass
peng1.canRun() #can run -> from subclass

