


def square(x):
    runningtotal = 0
    for counter in range(x):              # will loop 10 x. 'x' in this line does not need to be 10. Try using 15
        runningtotal = runningtotal + x   # running total

    return runningtotal                    # returns value back to the calling statement

# use of a for loop with range to pass in argument to the square function
for i in range(10,100,5):
    squareResult = square(i)               # calls the square function by iterating through the 'i' values
    print("The result of", i, "squared is", squareResult)
