#multiline statement

#explicit line continuation
b = 1 + 2 + 3 + \
    4 + 5 + 6
print(b) #21

#implicit line continuation within brackets
c = (1 + 2 + 3 + #using '\' here is optional
4 + 5 + 6)
print(c) #21

#multiline statements in one line
a = 1; b = 2; c = 3 #can't use commas
print(a, b, c) #1 2 3

#code block -> body of a func, loop, etc
