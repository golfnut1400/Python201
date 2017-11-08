
"""
Guessing a letter A-Z
check_guess() takes 2 string arguments: letter and guess (both expect single alphabetical character)
- if guess is not an alpha character print invalid and return False
- test and print if guess is "high" or "low" and return False
- test and print if guess is "correct" and return True
"""


def check_guess(letter, guess):
   # assert isinstance(letter, str)
   # assert isinstance(guess, str)
    if not letter.isalpha() or not guess.isalpha():
        print("Invalid")
        return False
    if (guess > letter):
        print("High")
        return False
    elif (guess < letter):
        print("Low")
        return False
    else:
        print("Correct")
        return True

letter = input("Enter a letter for user to guess: ")
guess = input("Enter a single letter from A - Z: ")

check_guess(letter, guess)
