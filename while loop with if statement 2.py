"""
Using while with a Boolean String
Program: Long Number
Create variables
int_num and get user input string of only digits
long_num and initialize it as an empty string

Create a while loop that runs as long as the input is all digits
Inside the while loop
add int_num to the end of long_num
get user input for int_num again (inside while loop this time)
After the loop exits
print the value of long_num"""

int_num = input("Enter digits only - ")
long_num = ''

while int_num.isdigit() == True:
    long_num = long_num + int_num  # add int_num to the end of long_num
    int_num = input("Enter digits again - ")
    if int_num.isdigit() == False:  # if not a digit to break
        break


print("Exiting program. Your last entry was not a digit. Here are the \n sequence of digits entered",long_num)
