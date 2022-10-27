#encapsulation -> only limited methods are accessed
class PC:

    def __init__(self):
        self.maxPrice = 20000

    def sell(self):
        print(self.maxPrice)
    
    def setMaxPrice(self, price):
        self.maxPrice = price
    
pc1 = PC()
pc1.sell() #20000

pc1.maxPrice = 30000 #changes the price
pc1.sell() #30000
pc1.setMaxPrice(40000) #changing price using setter func, same thing as before
pc1.sell() #40000
