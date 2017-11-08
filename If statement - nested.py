

response = input("Say 'Hello' by entering in textbox --> ")
response2 = input("Enter (Y/N)")

if response == '':
    if response2 == '':
        print("friendly nod")
    elif response2.lower() == 'y':
        print("Are you serious?")
    else:
        print("Let's try again")

if response.lower() == 'hello':
    if response2.lower() == 'y':
        print("Hello Stan")
    elif response2 == '' or response2 == 'n':
            print("Are you sure you did not say 'Hello'?")
    else:
        print("Goodbye!")




