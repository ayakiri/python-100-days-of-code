import random
import turtle as t
import colorgram


def position_tutle():
    new_turtle.penup()
    new_turtle.goto(-250, -250)


def draw_circle():
    new_turtle.color(random.choice(colours))
    new_turtle.pendown()
    new_turtle.begin_fill()
    new_turtle.circle(10)
    new_turtle.end_fill()
    new_turtle.penup()


def move():
    new_turtle.forward(50)


def change_row():
    new_turtle.left(90)
    new_turtle.forward(50)
    new_turtle.right(90)
    new_turtle.backward(500)


# extract colour palette
colours_extracted = colorgram.extract('image.jpg', 20)
colours = []

for colour_num in range(len(colours_extracted)):
    rgb = colours_extracted[colour_num - 1].rgb
    temp_tuple = (rgb[0], rgb[1], rgb[2])
    colours.append(temp_tuple)

t.colormode(255)

new_turtle = t.Turtle()
new_turtle.speed("fastest")

position_tutle()
for _ in range(10):
    for _ in range(10):
        draw_circle()
        move()
    change_row()

new_screen = t.Screen()
new_screen.exitonclick()
