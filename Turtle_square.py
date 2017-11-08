# Creating a square using directions

import turtle

window = turtle.Screen()
window.bgcolor("purple")
stan = turtle.Turtle()
stan.pensize(5)
stan.down()

stan.color("red")
stan.forward(150)
stan.left(90)
stan.forward(150)
stan.left(90)
stan.forward(150)
stan.left(90)
stan.forward(150)
stan.left(90)

window.exitonclick()
