"""Program: pre_word() Function¶
Function has a single string parameter that it checks s is a single word starting with "pre"

Check if word starts with "pre"

Check if word .isalpha()

if all checks pass: return True
if any checks fail: return False

Test
get input using the directions: enter a word that starts with "pre":

call pre_word() with the input string

test if return value is False and print message explaining not a "pre" word
else print message explaining is a valid "pre" word"""


# for word in SideMember:
#     if word.startswith('Base'):
#         print word

def pre_word(word):
    #print("hi")
    if word.startswith('pre'):
        if word.isalpha():
            return True
    else:
        return False


word = pre_word(input("Enter a word that starts with 'pre': "))
print()
print("Word start with 'pre'? ", word)
