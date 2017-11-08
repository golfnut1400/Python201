

# review and run code to test if a string is to be found in another string
menu = "salad, pasta, sandwich, pizza, drinks, dessert"
print('pizza' in menu)


# review and run code to test case sensitive examples
greeting = "Hello World!"
print("'hello' in greeting = ",'hello' in greeting)
print("'Hello' in greeting = ", 'Hello' in greeting)

# review and run code to test removing case sensitivity from a string comparison
greeting = "Hello World!"
print("'hello' in greeting = ",'hello' in greeting)
print("'Hello' in greeting = ", 'Hello' in greeting)
print("'hello' in greeting if lower used = ", 'hello'.lower() in greeting.lower())


# use of variable
# [] print 3 tests, with description text, testing the menu variable for 'pizza', 'soup' and 'dessert'
menu = "salad, pasta, sandwich, pizza, drinks, dessert, sushi"

print("Pizza in menu? =", 'pizza' in menu)
print("Soup in menu? =", 'soup' in menu)
print("Dessert in menu? =", 'dessert' in menu)


# Create a program where the user supplies input to search the menu
menu_ask = input("What item do you want to check?")
print (menu_ask)
print('menu_ask' in menu)


