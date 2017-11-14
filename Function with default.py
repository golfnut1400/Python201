

# function with a default

def another_message(message ="Hello Stan", number = 2):  # here are defaults
    while number <= 10:
        number += 2
        print("Here\'s to you and", message)



another_message("My message for you", 1)  # passing of two arguments to function


print()



# function with a default

def my_message(message ="Hello Stan", number = 2):  # here are defaults
    while number <= 10:
        number += 2
        print("Here\'s to you and", message)



my_message()  # no arguments passed to function

print()

# example of passing only one of the arguments to the function

def my_message(message ="Hello Stan", number = 2):  # here are defaults
    while number <= 10:
        number += 2
        print("Here\'s to you and", message)



my_message(message = 'I love pasta')  # no arguments passed to function


