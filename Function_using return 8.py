

# def short_rhyme(rhyme1, rhyme2):
#     print("Line 1:",rhyme1, "Line 2: ",rhyme2)
#
#
# # call function short_rhyme
# short_rhyme("Hello there coder", "Really that\'s it")
#
# # prints rhyme1 and rhyme2 on 2 lines
# print("This is a test" "\n" "Really")



# [ ] define (def) a simple function: title_it() and call the function
# - has a string parameter: msg
# - prints msg in Title Case
# #
# def title_it(msg):
#     print(msg.title())
#
#
# title_it("this is a title")
#
#
# # [ ] get user input with prompt "what is the title?"
# # [ ] call title_it() using input for the string argument
#
#
# msg = input("What is the title? ")
# title_it(msg)
#
#

# [ ] define title_it_rtn() which returns a titled string instead of printing
# [ ] call title_it_rtn() using input for the string argumetnt and print the result


def title_it_rtn(msg):
    return msg.title()

print(title_it_rtn(input("What is the tile of the movie? ")))
