#LAMBDA

#also called anonymous function -> defined without name
a = lambda x: x*2
print(a(3)) #6

#MAKING NEW LIST USING OLD LIST, LAMBDA AND FILTER

list1 = [1, 3, 5, 6, 9, 8]
list2 = list(filter(lambda x: x%2 == 0, list1))
print(list2) #[6, 8]

#DOUBLE EACH ITEM USING LAMBDA AND MAP

list3 = [1, 3, 5, 6, 9, 8, 6]
list4 = list(map(lambda x: x*2, list3))
print(list4) #[2, 6, 10, 12, 18, 16, 12]





