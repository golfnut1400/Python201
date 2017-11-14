
#Use of the keys() method.
# make note of the print out of the use of 'dict_keys
print("Use of keys()")
capitals = {'France':'Paris', 'Washington':'Seattle', 'UK':'London','Germany':'Berlin','Hawaii': 'Honolulu'}
print(capitals, len(capitals))
return_value = capitals.keys()  #returns the 'key' from each of the key:value pairs in the dictionay
print()
print("Returns the keys from above dictionary ",return_value)     #key:value pair removed arbitarily

print()
print("Use of list()")
# use of list()
capitals = {'France':'Paris', 'Washington':'Seattle', 'UK':'London','Germany':'Berlin','Hawaii': 'Honolulu'}
print(capitals, len(capitals))

return_value = list(capitals.keys())  # this will return a list
print()
print("Returns the keys from above dictionary ",return_value)     #key:value pair removed arbitarily


