from turtle import Turtle, Screen
import random


def create_turtles():
    for num in range(0, 7):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(turtle_colours[num])
        new_turtle.penup()
        new_turtle.goto(x=-430, y=turtle_positions[num])
        all_turtles.append(new_turtle)


is_race_on = False
winner = ""
screen = Screen()
screen.setup(900, 400)
turtle_colours = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
turtle_positions = [90, 60, 30, 0, -30, -60, -90]
all_turtles = []

bet = screen.textinput("Guess!", "Which turtle will win the race? Enter a colour")

create_turtles()

if bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        turtle_distance = random.randint(0, 10)
        turtle.forward(turtle_distance)
        if turtle.xcor() > 430:
            is_race_on = False
            winner = turtle.color()[0]

print(f"The winner is {winner} turtle!")

if bet.lower() == winner.lower():
    print("Congrats, you won!")
else:
    print("You lost the bet")


screen.exitonclick()

