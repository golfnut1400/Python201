"""while True
[ ] Program: Get a name forever ...or until done
create variable, familar_name, and assign it an empty string ("")
use while True:

ask for user input for familar_name (common name friends/family use)

keep asking until given a non-blank/non-space alphabetical name is received (Hint: Boolean string test)
break loop and print a greeting using familar_name


"""

familar_name = ''

while True:
    familar_name = input("Enter a (common name friends/family use): ")
    if familar_name == '':
        break


print(familar_name)
