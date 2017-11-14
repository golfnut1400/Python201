
# this function passes arguments to the function. No value is returned


def multiple_display(message,times):
    for i in range(times):  #use of range to loop as many times as the stated argument
        print(message)

        # note there is no return to the calling statement



def another_message(message, number):
    while number <= 10:
        number += 2
        print("Here\'s to you and", message)


multiple_display("Hello Stan", 7)
another_message("My message for you", 1)
