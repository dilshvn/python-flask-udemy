#used in generator
#returns multiple items
def generator():
    for i in range(6):
        yield i

#print(generator()) doesn't print anything
for i in generator():
    print(i)
