import random
from turtle import Turtle

COLORS = ["pink", "hot pink", "purple", "blue"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Cars:
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT

