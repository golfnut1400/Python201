
while True:
    f_name = input("Enter a single word first name: ").capitalize()     # takes an imput and capitalizes the first letter

    if f_name.isalpha():    # check if the input is an alpha
        break
    else:
        print(f_name, "is not a single word \n")    # \n cursor jumps to next line




print("Welcome", f_name, "!")
