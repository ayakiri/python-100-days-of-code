import turtle
from turtle import Turtle, Screen


def forward():
    new_turtle.forward(10)


def backward():
    new_turtle.backward(10)


def clockwise():
    new_turtle.right(5)


def counter_clockwise():
    new_turtle.left(5)


def clear():
    new_turtle.reset()


new_turtle = Turtle()
new_screen = Screen()

new_screen.listen()
new_screen.onkey(key="w", fun=forward)
new_screen.onkey(key="s", fun=backward)
new_screen.onkey(key="a", fun=counter_clockwise)
new_screen.onkey(key="d", fun=clockwise)
new_screen.onkey(key="c", fun=clear)

new_screen.exitonclick()

