import turtle              # 1.  import the modules
import random

wn = turtle.Screen()       # 2.  Create a screen
wn.bgcolor('lightblue')

lance = turtle.Turtle()    # 3.  Create two turtles
andy = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')

andy.up()                  # 4.  Move the turtles to their starting point
lance.up()
andy.goto(-250,20)
lance.goto(-250,-20)


for ran in range(5): #loops 5x

    x = random.randrange(1,100,2)  # start, stop, step
    andy.forward(x)
    y = random.randrange(1,100,3)
    lance.forward(y)


wn.exitonclick()
