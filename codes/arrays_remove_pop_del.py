# numpy arr > arr

arr = ["car", "bus", "bike"]

# remove item
arr.remove("car")
print(arr)
# o/p: ['bus', 'bike']

# use pop to remove by index
arr.pop(0)
print(arr)
# o/p: ['bike']

# del is similar to pop
arr = ["car", "bus", "bike"]
del arr[1]
print(arr)
# o/p: ['car', 'bike']