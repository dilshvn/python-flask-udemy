class Base1:
    def funcBase1(self):
        print('base1')

class Base2:
    def funcBase2(self):
        print('base2')

class Base3:
    def funcBase3(self):
        print('base3')

class MultiDerived(Base1, Base2, Base3): #multidervied class, 3 base (super) classes
    def funcMultiDerived(self):
        print('multiderived')

md1 = MultiDerived() #md1 is an object
md1.funcBase1() #base1
md1.funcBase2() #base2
md1.funcBase3() #base3