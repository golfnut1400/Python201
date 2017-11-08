

"""update the multiply() function to multiply or divide

single parameter is operator with arguments of * or / operator

default operator is "*" (multiply)

return the result of multiplication or division

if operator other than "*" or "/" then return "Invalid Operator"""
#



def multiply(operator = 'x'):
    x = int(input("Enter an integer: "))   # input is cast from a string to an integer
    x2 = int(input("Enter a second interger: "))
    # operator = input("Enter operator ('x','/'): ")
    if operator == 'x':
        result = x * x2
    elif operator == '/':
        result = x/x2
    else:
        result = ("Invalid Operator")
    return result

print("The value is: ",multiply('1'))
print("The value is: ",multiply('x'))
print("The value is: ",multiply('/'))
print("The value is: ",multiply(''))
