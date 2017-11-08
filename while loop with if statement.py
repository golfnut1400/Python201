"""while True¶
[ ] Program: Get a name forever ...or until done
create variable, familar_name, and assign it an empty string ("")

use while True:
ask for user input for familar_name (common name friends/family use)
keep asking until given a non-blank/non-space alphabetical name is received (Hint: Boolean string test)
break loop and print a greeting using familar_name"""

familar_name = ""

while True:
    # use .lstrip to handle the case if user enters spaces before the string i.e.(   Stan)
    familar_name = (input("Enter (common name friends/family use): - ")).lstrip()
    if familar_name == "":
        print("Try again")
    # if users enters a common name, the program will breack and print the name
    else:
        break

print("Hello",familar_name +"!")
