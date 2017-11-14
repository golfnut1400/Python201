"""
update([other])
Update the dictionary with the key/value pairs from other, overwriting existing keys. Return None.

update() accepts either another dictionary object or an iterable of key/value
pairs (as tuples or other iterables of length two). If keyword arguments are specified,
the dictionary is then updated with those key/value pairs: d.update(red=1, blue=2).
"""




#Use of the update() method.

print("Use of update()")
capitals = {'France':'Paris', 'Washington':'Seattle', 'UK':'London','Germany':'Berlin','Hawaii': 'Honolulu'}
more_capitals = {'Oregon':'Portland', "Mexico": 'Mexico City' }

return_value = capitals.update(more_capitals)       # updating capitals with items in more_capitals. See above 'None'
print(return_value)
print(capitals)
print(more_capitals)



