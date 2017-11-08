

"""Program: [ ] 3 Guesses
use nested if statements complete the flowchart code

create a birds string variable with the names of 1, 2, 3 or more birds to make it easier

get bird_guess input and use bird_guess in bird_names to generate Boolean True/False

if the the guess is wrong (False) create a sub test until the user has had 3 guesses
"""

""
# > the_number = random.randrange(100) + 1
# >
# > guess = int(raw_input("Take a guess: "))
# > tries = 1
# >
# > # guessing loop
# > while (guess != the_number):
# >     if tries > 5:
# >         break
# >     elif guess > the_number:
# >         print "Lower..."
# >     elif guess < the_number:
# >         print "Higher..."
# >
# >     guess = int(raw_input("Guess again:"))
# >     tries += 1
# >
# >
# > # message of congratulations
# > print "You guessed it! The number was", the_number
# > print "And it only took you", tries, "tries!\n"""

birds_name = "1, 2, 3,"
bird_guess = input("Take a guess: ")
bird_guess = bird_guess in birds_name
print(bird_guess)
count = 0

if (bird_guess == 'False'):
    if count < 3:
        print("Try again")
        bird_guess = input("Take another guess: ")
        count = count + 1



#print(bird_guess)

##print("Correct! You must be pychic")


