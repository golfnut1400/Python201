# Asks the user for a number that is divisible by 2
# Keep asking until the user provides a number that is divisible by 2.

#
# print 'Question 4. \n'
#
# num = float(raw_input('Enter a number that is divisible by 2: '))
#
# while (num%2) != 0:
#     num = float(raw_input('Please try again: '))
# print 'Congratulations!'




print ('Question 4. \n')

prompt = 'Enter a number that is divisible by 2: '

while True:
    data = input(prompt)
    if data:
        try:
            number = float(data)
        except ValueError:
            print ('Invalid input...')
        else:
            if number % 2 == 0:
                print ('Congratulations!')
                break
        prompt = 'Please try again: '
    else:
        # allow the user to exit by entering nothing
        print ('Goodbye!')
        break
