

import turtle

window = turtle.Screen()
window.bgcolor("blue")
stan = turtle.Turtle()
stan.color("yellow")
stan.pensize(5)
stan.down()


for var in ["black","purple","black","purple"]:  # color of the sides of the sqare
    stan.color(var)  #uses the loop varible for each item in the list
    stan.forward(100)
    stan.left(90)

window.exitonclick()
