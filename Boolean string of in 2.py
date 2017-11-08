# project: "guess what I'm reading"

# 1[ ] get 1 word input for can_read variable
can_read = input("Enter 1 word: ")


# 2[ ] get 3 things input for can_read_things variable
can_read_things = input("Enter 3 words: ")

# 3[ ] print True if can_read is in can_read_things
print(can_read in can_read_things)



# [] challenge: format the output to read "item found = True" (or false)
# hint: look print formatting exercises
print("The item",can_read, "is found:",can_read in can_read_things)
