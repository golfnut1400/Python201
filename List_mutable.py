

# Example showing that a list is mutable
# showing the id of the list

list1 = [2,3,4,5]
print(list1, id(list1))

list1[0] = 11  # changing list1 at index 0 to equal 11
print(list1, id(list1))
list1[3] = 12
print(list1, id(list1))
# list1[4] = 13   # see what happens when attempting to add 13 to index 4 (index out of range error)
list1.append(101)   # adding 101 to list1
print(list1, id(list1))

print()
# printing the id of an idividual item
print("Value at index 0: ",list1[0], "id of idex 0", id(list1[0]))
