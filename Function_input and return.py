

# create and call make_doctor() with full_name argument from user input - then print the return value

def make_doctor(name):
    add_doctor = "Doctor "+name
    return add_doctor


full_name = input("What is your full name?")

print(make_doctor(full_name))

