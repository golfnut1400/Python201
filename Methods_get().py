

"""get(key[, default])
Return the value for key if key is in the dictionary, else default.
If default is not given, it defaults to None, so that this method never raises a KeyError."""


#Use of the get() method.
# make note of the print out of the use of 'dict_keys
print("Use of keys()")
capitals = {'France':'Paris', 'Washington':'Seattle', 'UK':'London','Germany':'Berlin','Hawaii': 'Honolulu'}
print(capitals, len(capitals))
return_value = capitals.get('UK')  #returns the 'get'
return_value = capitals.get('Spain')    #Spain no in the dictionary


capitals = {'France':'Paris', 'Washington':'Seattle', 'UK':'London','Germany':'Berlin','Hawaii': 'Honolulu'}

try:
    print(capitals['UK'])
    print(capitals['Spain'])

except KeyError:
    print("You have tried to enter an item not in the dictionary")


