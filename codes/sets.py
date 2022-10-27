#sets can be created using {}
#no duplicates, no indexing, can be iterated
#can have mixed datatypes
#set is mutable, but can't have mutable items (Ex: list)
#set()

#.add adds one item, .update adds multiple
set1 = {1, 3, 2, 6}
set1.add(4)
print(set1)
#o/p: {1, 2, 3, 4, 6}
#.update take iterables (Ex: list, set)
set1.update([7, 8, 9])
print(set1)
#o/p: {1, 2, 3, 4, 6, 7, 8, 9}

#.discard -> removes item if available, else -> no error
#.remove -> removes item if available, else -> error
#.pop -> removes random item
#.clear -> removes all items, empty set exists
set1.discard(1)
print(set1)
#o/p: {2, 3, 4, 6, 7, 8, 9}

#.union or '|'
#.intersection or '&'
#.difference or '-' -> in set1 but not in set2 -> set difference
#.symmertric_difference or '^' -> without intersection -> symmetric difference

#in, not in
#len, max, min, sorted
#sorted returns a list, not set

#frozenset -> immutable sets
set2 = frozenset([1, 2, 5, 7])

