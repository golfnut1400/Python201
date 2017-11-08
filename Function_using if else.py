


# Function to test if each of the 3 strings below starts with a 'w'
def w_start_test(string):
    if string.lower().startswith('w'): # added a .lower() in the case the string begins with a capital 'W'
        print("The string-", string, "- Starts with 'w'")
    else:
        print("The string-", string, "- Does not start with 'w'")

# setting each varibles
test_string_1 = "Welcome"
test_string_2 = "I have $3"
test_string_3 = "With a function it's efficient to repeat code"

# [ ] Test the 3 string variables provided by calling w_start_test()

w_start_test(test_string_1)
w_start_test(test_string_2)
w_start_test(test_string_3)
