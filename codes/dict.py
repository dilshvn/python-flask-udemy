#indexed with keys
#mutable, keys are immutable objects
dict = {1:'car', 2:'bus', 3:'train'}
print(dict.get(2)) #returns value of key '2', returns 'none' if unavailable
print(dict[2]) #returns value of key '2', returns error if unavailable 
#o/p: bus

dict[1] = 'tuktuk' #reassigning value
dict[4] = 'suv' #adding new key, value pair

dict.pop(4) #removing specific item
del dict[2] #removing specific item, similar to pop 
#o/p: {1: 'tuktuk', 2: 'bus', 3: 'train'}
dict.popitem() #removing random item
dict.clear() #remove all items, returns {}
del dict #delete dictionary

dict1 = {x: x*x for x in range(6)} #dict creation using comprehensions
print(dict1)
#o/p: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#in, not in -> only checks for keys, not values

#iterates and returns only values
for i in dict1:
    print(i)

#len -> length of dict -> 1 key, value pair is counted as 1 item

print(sorted(dict1)) #prints only keys (sorted)

