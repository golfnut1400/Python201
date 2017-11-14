

# dictionary are key:value pairs
# keys that are string are immutable (cannot change)
# values that are strings, numbers, other lists are mutable

capitals = {'France':'Paris', 'Washington':'Seattle', 'UK':'London','Germany':'Berlin','Hawaii': 'Honolulu'}
print(capitals, len(capitals))
print()

numbers = {'one': 100, 'two': 200,'three': 300}
print(numbers)
print(numbers.values())


# lists

list1 = [1,2,3, [10,11,12]]
print(list1)
print(list1[1])
print(list1[3])  # prints out the list withing list1
