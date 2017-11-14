
"""items()
Return a new view of the dictionary’s items ((key, value) pairs). See the documentation of view objects."""

#Use of the item() method.
# make note of the print out of the use of 'dict_keys
print("Use of items()")
capitals = {'France':'Paris', 'Washington':'Seattle', 'UK':'London','Germany':'Berlin','Hawaii': 'Honolulu'}
print(capitals, len(capitals))
return_value = capitals.items()  # use of items()
print(return_value)   # returns tuples of key:value pairs in a list noted by the '[ ] ' brackets
                        # note in the print 'dict_items'


print()
capitals = {'France':'Paris', 'Washington':'Seattle', 'UK':'London','Germany':'Berlin','Hawaii': 'Honolulu'}
print(capitals, len(capitals))
return_value = list(capitals.items())  #returns the 'list()'
print(return_value)   # returns tuples of key:value pairs in a list noted by the '[ ] ' brackets
                        # not in the print -- this returns a list
