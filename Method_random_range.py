

import random

 # Select random float between 0.0 and 1.0
myNumber = random.random()
print(myNumber)


# prints numbers from 5 to 249
for ran in range(5,250):
    print(ran)


diceThrow = random.randrange(1, 7)       # return an int, one of 1,2,3,4,5,6
print(diceThrow)



# Use of randrange in a function

def request_range(start, end):
    x = random.randrange(start,end)     # uses the randrange() and creates a random number from the 2 arguments
    print(x)


request_range(1,1000)        # calls the request_range function and passes the 2 arguments

