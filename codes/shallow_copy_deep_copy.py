#COPYING USING ASSIGN

list1 = [[1, 2, 3], [4 , 5, 6], [7, 8, 9]]
list2 = list1

print(id(list1) == id(list2)) #True

list1.append([10, 11, 12])
print(list2) #[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print(list1 == list2) #True -> list2 also changes when list1 is changed

print(id(list1) == id(list2)) #True

#CREATING COPY USING SHALLOW COPY

import copy

list3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list4 = copy.copy(list3) #shallow copy
print(list3 == list4) #True

#ADDING ELEMENTS TO LIST USING SHALLOW COPY

list3.append([4, 4, 4])
print(list3 == list4) #False -> list4 doesn't change when list3 is changed in shallow copy
print(list3) #[[1, 2, 3], [4, 5, 6], [7, 8, 9], [4, 4, 4]]
print(list4) #[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#ADDING NEW NESTED OBJECT USING SHALLOW COPY

list3[1][1] = 'AA'
print(list3) #[[1, 2, 3], [4, 'AA', 6], [7, 8, 9], [4, 4, 4]]
print(list4) #[[1, 2, 3], [4, 'AA', 6], [7, 8, 9]] -> list4 also changes when element is assigned (even in shallow copy)

list4[1][1] = 'BB'
print(list3) #[[1, 2, 3], [4, 'BB', 6], [7, 8, 9], [4, 4, 4]] -> list3 also changes when list4 is changed in shallow copy
print(list4) #[[1, 2, 3], [4, 'BB', 6], [7, 8, 9]]

list3[3][1] = 'CC'
print(list3) #[[1, 2, 3], [4, 'BB', 6], [7, 8, 9], [4, 'CC', 4]]
print(list4) #[[1, 2, 3], [4, 'BB', 6], [7, 8, 9]] -> list4 doesn't change because list4 doesn't have that object

#only the reference of the nested copy is copied in shallow copy

#DEEP COPY

import copy

list5 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
list6 = copy.deepcopy(list5)

print(list5) #[[1, 1, 1], [2, 2, 2], [3, 3, 3]]
print(list6) #[[1, 1, 1], [2, 2, 2], [3, 3, 3]]
print(id(list5) == id(list6)) #Flase -> IDs are different in deep copy -> new object is created

#ADDING NEW NESTED OBJECT IN LIST USING DEEP COPY

list5[1][0] = 'BB'

print(list5) #[[1, 1, 1], ['BB', 2, 2], [3, 3, 3]]
print(list6) #[[1, 1, 1], [2, 2, 2], [3, 3, 3]] -> list6 doesn't change when assigned in deep copy

