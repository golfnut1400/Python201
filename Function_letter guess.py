


#### needs work


def letter_guess(guess, answer):

    #guess = input("Guess a letter: ")
    count = 1
    print("Test", guess, answer)
    while count < 3 and guess.lower() != answer:
        count = count + 1
        guess = input("Guess a letter: ")
        return guess



# call function letter_guess

myguess = input("Guess a letter: ")   # user is asked to enter a letter
letter_guess(myguess, 'a')   # 'a' is the argument passed to 'answer'
print("Your guess:",guess, "is correct!")
