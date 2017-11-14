
#Use of the popitem method

capitals = {'France':'Paris', 'Washington':'Seattle', 'UK':'London','Germany':'Berlin','Hawaii': 'Honolulu'}
print(capitals, len(capitals))
return_value = capitals.popitem()
print(return_value)     #key:value pair removed arbitarily
print(capitals, len(capitals))



