

# [ ] Create the Animal Names program, run tests


all_animals = []
counter = 0


while counter < 4:
    animal_name = input("Enter name of an animal - ")
    #print(animal_name)
    counter = counter + 1
    all_animals.append(animal_name)

    if animal_name == 'exit':
        print("So long")
        break

    if animal_name == '':
        print("no animals entered")
        break

print("You entered: ",all_animals)
