"""Create function age_20() that adds or subtracts 20 from your age for a return value
based on current age (use if)

call the funtion with user input and then use the return value in a sentence
example age_20(25) returns 5: > "5 years old, 20 years difference from now"""


def age_20(current_age):
    if current_age <=20:
        age_plus = current_age + 20    # addes 20 to current age
        return age_plus
    else:
        age_minus = current_age - 20    # subtracts 20 from current age
        return age_minus

current_age = int(input("What is your current age? "))
result =age_20(current_age)
print()
print (result, "years old, 20 years difference from now")


