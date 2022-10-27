#isinstance -> checks type and returns boolean
print(isinstance(100, float)) #False
print(isinstance(100.0, float)) #True
print(isinstance(5 + 6j, complex)) #True

#0b, 0x, 0o or 0B, 0X, 0O-> binary, hex, octal
print(0b1101) #13
print(0xab) #171
print(0o23) #19

#type conversion -> int(), float()

print(1.2 * 2.5 == 3.0) #True
print(0.1 + 0.2 == 0.3) #False -> 0.1 + 0.2 = 0.3000000000004
#to fix this,
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.2') == 0.3) #True

from fractions import Fraction
print(Fraction(1.5)) #3/2
print(Fraction(1, 5)) #1/5
print(Fraction(5)) #5

#math module
#.pi, .cos(), .exp(), .factorial(), .sinh()
# abs() -> no need to use math.abs()
#.log() -> ln() -> natural log
#.log10() -> 10th base
import math

#random module
import random
print(random.randrange(5, 15)) #random int in (5, 15) range
print(random.choice(['a', 'b', 'c', 'd']))
print(random.shuffle(['a', 'b', 'c', 'd'])) #shuffles a list
print(random.random())