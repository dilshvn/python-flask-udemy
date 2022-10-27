class ComplexNumber:
    #__init__ is a constructor
    def __init__(self, real = 0, img = 0):
        print("ComplexNumber constructor executing...")
        self.real = real
        self.img = img
    #this is a method/function
    def displayComplex(self):
        print("{} + {}j".format(self.real, self.img))

complex = ComplexNumber(4, 6)
complex.displayComplex()
#o/p: 4 + 6j