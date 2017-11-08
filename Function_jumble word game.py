

 #Word Jumble Game
import random
import string

def jumbled():
        words = ['Jumble', 'Star', 'Candy', 'Wings', 'Power', 'String', 'Shopping', 'Blonde', 'Steak', 'Speakers', 'Case', 'Stubborn', 'Cat']
        count = 0                       ## initialize the count value.
        flag = True                    ## I have used flag as to when to stop executing the program (depending on the value of flag)
        while flag:                    ## Let it run infinitely till user gets right answer!
            word = (random.choice(words))
            print(word)
            jumble = list(word)
            random.shuffle(jumble)
            scrambled = "".join(jumble)
            print ('\n',scrambled, '\n')
            print(scrambled)

            guess = input('Guess the word: ').lower()

            #if guess.lower() == word:    ## I have used guess.lower() to match with word.lower(). You had missed out to convert guess to lower case!
            if word == guess:
                print ('\n','Correct!')
                count+=1                          ## increment the counter
                flag = False
                print ("Number of guesses you took to get right answer=",count)  ## print the count
            else:
                print ('\n','Try again!','\n')
                count+=1                          ## increment count for every wrong answer
                print ("You had %d tries" %count)   ## let user know how many tries he had.


jumbled()
