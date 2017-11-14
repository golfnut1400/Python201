
# guess the number

number_guess = "0"  # note value set to string
secret_number = "5" # note value set to string

while True:
    number_guess = input("Guess a number 1 - 5? ")
    if number_guess == secret_number:
        print("Yes,", number_guess, "is correct!\n")
        break   # break is used to break out of the loop and returns code followed by the indentation
    else:
        print(number_guess, "is incorrect\n")
