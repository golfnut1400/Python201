
# Example 1
def isDivisible(x, y):
    if x % y == 0:      # if as part of the function
        result = True
    else:
        result = False

    return result

print("Example 1:",isDivisible(10, 5))


# Example 2
def isDivisible(x, y):
    return x % y == 0

if isDivisible(10, 5):      # if outside of the function. Calls the 'isDivisible' function
    print("Example 2:"+"That works")
else:
    print("Example 2:"+"Those values are no good")



