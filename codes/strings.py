#can use ', ", ''' or """ for strings
#strings are immutable

str = 'abcd'
print(str[3:1]) #returns nothing

#in, not in

#enumerate
print(list(enumerate('university')))
#o/p: [(0, 'u'), (1, 'n'), (2, 'i'), (3, 'v'), (4, 'e'), (5, 'r'), (6, 's'), (7, 'i'), (8, 't'), (9, 'y')]
#here, items are tuples

#escaping
print('I\'m')
print("I'm")
print('''I'm''')
#all 3 codes prints the same thing -> I'm
print('\\') #o/p: \

#\n -> new line
#\t -> tab (8 spaces)
#\x -> hexadecimal -> Ex: \x41 = A

#formatting
print('{}{}{}'.format('a', 'b', 'c')) #o/p: abc
print('{2}{1}{0}'.format('a', 'b', 'c')) #o/p: cba
print('{x}{y}{z}'.format(x = 'b', y = 'a', z = 'c')) #o/p: bac

print('{0:b}'.format(10)) #o/p: 101010 -> binary value of 10
print('{0:e}'.format(1234)) #o/p: 1.234000e+03 -> exponential value
print('{0:.2f}'.format(12.3456)) #o/p: 12.35 -> rounds to 2nd decimal point
print('{0:.2f}'.format(11/5)) #o/p: 2.20

#.lower, .upper, .find, .replace
print('ABCDE'.find('C')) #2 -> index of C
print('ABCDE'.find('c')) #-1 -> no results, case sensitive
#.replace is also case sensitive

