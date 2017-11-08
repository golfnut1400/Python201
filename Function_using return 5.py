"""

create and test fishstore()

fishstore() takes 2 string arguments: fish & price
fishstore returns a string in sentence form
gather input for fish_entry and price_entry to use in calling fishstore()
print the return value of fishstore()
example of output: Fish Type: Guppy costs $1

# [ ] create, call and test fishstore() function
# then PASTE THIS CODE into edX



"""


def fishstore(fish,price):
    return print("Fish Type:", fish_entry, "costs $", price_entry)


fish_entry = input("Enter fish:")
price_entry = input("Enter price:")

# call fishstore() function here
fishstore(fish_entry, price_entry)
