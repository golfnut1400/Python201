

import random
class RollTheDice(object):

    def __init__(self):
        self.min = 1
        self.max = 6
        super(RollTheDice, self).__init__()

    def ask_something(self):
        while True:
            userInput = str(input("Roll Again? Yes(Y) or No(N)" + "\n"))
            if (userInput == "Yes" or userInput == 'Y'):
                self.rollDice()
            else:
                print("You didn't type 'Yes' or 'Y' no roll for you. Bye....")
                exit()

    def rollDice(self):
        print ("Rolling the dices...")
        print ("The values are....")
        print (random.randint(self.min, self.max))
        print (random.randint(self.min, self.max))

RollTheDiceObject = RollTheDice()
RollTheDiceObject.ask_something()
