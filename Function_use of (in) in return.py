

# [ ] fix the sequence of the code to remove the NameError


def hat_available(color):
    hat_colors = 'black, red, blue, green, white, grey, brown, pink'
    return(color.lower() in hat_colors)     # use if 'in' as part of the return

have_hat = hat_available('green')       # calls function and passing 'green' argument to the 'color' parameter.
                                        #  'green' is hard coded.
                                        # best practice is to use an 'input()' and assign to a variable

print('Hat available is', have_hat)
