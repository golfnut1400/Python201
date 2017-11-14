

"""
R = Red
O = Orange
Y = Yellow
G = Green
B = Blue
I = Indigo
V = Violet
else print "no match"""

rainbow_color = ['Red','Orange','Yellow','Green','Blue','Indigo','Violet']


def select_color(my_color):
    for item in rainbow_color:
        if my_color in item:
            print(item)
            return (item)
    print("Sorry, No Match")


my_color = input("Enter your favorite color (Use only first letter of color (i.e.'R' = Red): ")
print("Your favorite color:", select_color(my_color))

