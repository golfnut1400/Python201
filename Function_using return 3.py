


# [ ] create function bird_available
def bird_avaiable(bird):
    bird_types = 'crow robin parrot eagle sandpiper hawk piegon'
    return (bird in bird_types)

# [ ] user input
bird = input("What bird type were you hoping to see?")

# [ ] call bird_available
my_birds = bird_avaiable(bird)

# [ ] print availbility status
print('Bird type avaiable?:', my_birds)
