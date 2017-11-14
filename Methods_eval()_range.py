

calculation = input("Type in function for 'y': ")       # i.e. 2 * x + 4

for x in range(0,100,10):   # start at 0 and up to 100 with a step of 10
    print("For x = ", x, ": y = ",eval(calculation))
