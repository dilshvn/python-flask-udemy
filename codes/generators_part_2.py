#generators with a loop
def reverse_string(string):
    for i in range(len(string) - 1, -1, -1): #loops from (len-1) to 0 with -1 step
        yield string[i] #output is a sequence

print(reverse_string('hello')) #returns nothing
print(list(reverse_string('hello'))) #['o', 'l', 'l', 'e', 'h']

for i in reverse_string('hello'):
    print(i)
'''
o/p:
o
l
l
e
h
'''
