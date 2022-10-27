#nested dict
people = {1:{'name':'John', 'age':'25', 'sex':'male'}, 2:{'name':'Marie', 'age':'22', 'sex':'female'},}

print(people[1]['name']) #John

#adding elements to dict
people[3] = {}
people[3]['name'] = 'Dilshan' 
people[3]['age'] = '25'

#deleting elements from dict
del people[3]
del people[1]['name'], people[2]['age'] #deleting multiple elements

print(people.items())
#o/p: dict_items([(1, {'age': '25', 'sex': 'male'}), (2, {'name': 'Marie', 'sex': 'female'})])

#iterating through elements
for i, j in people.items():
    print(i) #1, 2 -> keys
    print(j) #{'age': '25', 'sex': 'male'}, {'name': 'Marie', 'sex': 'female'} -> values
    for k in j:
        print(j[k]) #25, male, Marie, female




