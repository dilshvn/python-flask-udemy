#polymorphism
class Parrot:
    def canFly(self):
        print('can fly')

    def canSwim(self):
        print("can't swim")

class Penguin:
     
    def canFly(self):
        print("can't fly")

    def canSwim(self):
        print('can Swim')

#common interface
def flying_bird_test(bird):
    bird.canFly() #both Parrot and Penguin classes have these methods, but can be used -> polymorphism
    bird.canSwim()

#instantiating objects
parrot1 = Parrot() 
penguin1 = Penguin()

flying_bird_test(parrot1)
print() #prints empty line
flying_bird_test(penguin1)