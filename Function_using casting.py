"""define function multiply(), and within the function:
gets user input() of 2 strings made of whole numbers
cast the input to int()
multiply the integers and return the equation with result as a str()
return example
9 * 13 = 117"""


# [ ] create and test multiply() function

def multiply():
    x = int(input("Enter an integer: "))   # input is cast from a string to an integer
    x2 = int(input("Enter a second interger: "))
    result = x * x2
    return result


print("The value is: ",multiply())
