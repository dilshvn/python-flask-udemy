#using for loop

list1 = []

for i in 'human':
    list1.append(i)

print(list1) #['h', 'u', 'm', 'a', 'n']

#using list comprehensions

list2 = [i for i in 'human']
print(list2) #['h', 'u', 'm', 'a', 'n']

#using lambda

list3 = list(map(lambda i: i, 'human'))
print(list3) #['h', 'u', 'm', 'a', 'n']

#list comprehensions with 'if'

list4 = [i for i in range(20) if i%2 == 0] #even numbers
print(list4) #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

#list comprehensions with nested 'if'

list5 = [i for i in range(100) if i%2 == 0 if i%5 == 0]
print(list5) #[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

#list comprehensions with if-else

list6 = ['even' if i%2 == 0 else 'odd' for i in range(10)]
print(list6) #['even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd']

#transporting a matrix using list comprehensions

mat1 = [[1, 2],
        [3, 4],
        [5, 6],
        [7, 8]]

trans1 = [[row[i] for row in mat1] for i in range(2)]
print(trans1) #[[1, 3, 5, 7], [2, 4, 6, 8]] -> transpose of mat1