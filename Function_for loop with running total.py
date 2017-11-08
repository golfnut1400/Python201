"""To square the value of n, we will repeat the process of updating a running total n times. To update the running total,
we take the old value of the “running total” and add n. That sum becomes the new value of the “running total"""


def square(x):
    runningtotal = 0
    for counter in range(x):              # will loop 10 x. 'x' in this line does not need to be 10. Try using 15
        runningtotal = runningtotal + x   # running total

    return runningtotal                    # returns value back to the calling statement


toSquare = 10
squareResult = square(toSquare)            # calls on the 'square' functiona and passes '10' to x
print("The result of", toSquare, "squared is", squareResult)
