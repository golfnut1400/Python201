

import random

 # Select random float between 0.0 and 1.0
myNumber = random.random()
print("Your random number:", myNumber)

print()

# prints numbers from 5 to 249
print("start")
for random_number in range(5,250):
    print('\t',random_number)
print("end")

print()

diceThrow = random.randrange(1, 7)       # return an int, one of 1,2,3,4,5,6
print("Your dice number:",diceThrow)


print()
# Use of randrange in a function

def request_range(start, end):
    x = random.randrange(start,end)     # uses the randrange() and creates a random number from the 2 arguments
    print("Your range number:",x)

request_range(1,1000)        # calls the request_range function and passes the 2 arguments

