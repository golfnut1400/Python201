


import turtle

window = turtle.Screen()
window.bgcolor("blue")
stan = turtle.Turtle()
stan.shape('triangle')   # arrow, blank, circle, classic, square, triangle, turtle
stan.color("yellow")
stan.pensize(1)
stan.down()

for var in [1, 2, 3, 4]:  # using list with 4 sides
    stan.forward(100)
    stan.left(90)

window.exitonclick()




