#operator overloading
#all method here are super private
class Point:

    def __init__(self, x = 0, y = 0): #constructor with default args
        self.x = x
        self.y = y

    def __str__(self):
        return(str(self.x) + ' ' + str(self.y)) #output should be a string
    
    #overloading + operator
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    #overloading < operator
    def __lt__(self, other):
        self_mag = (self.x**2) + (self.y**2) #checks magnitude
        other_mag = (other.x**2) + (other.y**2)
        return self_mag < other_mag #returns boolean

point1 = Point(1, 2) #initiates -> constructor __init__ runs
point2 = Point(4, 5)

print(point1) #1 2 -> __str__ runs
print(point1.__str__()) # 1 2, similar to above method
print(point2) #4 5
print(point2.__str__()) #4 5

print(point1 < point2) #True
print(point1.__lt__(point2)) #True, similar to above method

print(point1 + point2) #5 7
print(point1.__add__(point2)) #5 7, similar to above method