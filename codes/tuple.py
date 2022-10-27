#elements in tuple can't be changed -> immutable -> can be used for dict keys
#use () to make a tuple, can be created without () too
#faster than lists

tup = (1, 3, 4)
tup1 = 1, 3, 4
print(tup == tup1)
#o/p: True

#tuple unpacking
a, b, c = tup1
print(a)
#o/p: 1

#tuples are indexed -> can be iterated
print(tup1[1])
#o/p: 3

tup2 = ('car', 3)
print(tup2[0][2])
#o/p: r

#tuples can be sliced
#tuples can be reassigned
#tuples can be deleted using 'del', not tuple items

#tuples can be concatenated
print(tup1 + tup2)
#o/p: (1, 3, 4, 'car', 3)

#tuple attributes -> .count, .index
#tuple functions/methods -> max, min, sorted, len
#tuple operations -> in, not in