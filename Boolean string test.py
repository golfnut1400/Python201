
"""Vehicle tests
get user input for a variable named vehicle
print the following tests results
check True or False if vehicle is All alphabetical characters using .isalpha()
check True or False if vehicle is only All alphabetical & numeric characters
check True or False if vehicle is Capitalized (first letter only)
check True or False if vehicle is All lowercase
bonus print description for each test (e.g.- "All Alpha: True")

"""

vehicle = input("Enter a vehicle name: - ")

v_alpha = vehicle.isalpha()
print("All Alpha: - ",v_alpha)

v_alphanum = vehicle.isalnum()
print("Name contain both alpha & num: - ",v_alphanum)

v_cap = vehicle[0].isupper()   # note how the [0] index is used
print("Vehicle cap(first letter only): - ", v_cap)

v_lc = vehicle.islower()
print("All lowercase: - ",v_lc)
