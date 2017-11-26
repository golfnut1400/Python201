
print("I am string BEFORE the iteration")
print()

for count in (0, 1, 2):
    print("I am a string WITHIN the iteration")
    print("The count value is", count)
    print()

print("I am string AFTER the iteration - DONE")

print()
print()

# example using a list
print("I am string BEFORE the iteration using a list")
print()

my_list = [0, 1, 2]
print("Here is my list:",my_list)

for count in my_list:
    print("I am a string WITHIN the iteration using a list")
    print("The count value is", count)
    print()

print("I am string AFTER the iteration using a list - DONE")



# example using a range
print("I am string BEFORE the iteration using a range")
print()

my_range = range(10, 15, 1)     # range (start, end, step)

for count in my_range:
    print("I am a string WITHIN the iteration using a range")
    print("The count value is", count)
    print()

print("I am string AFTER the iteration using a range - DONE")
