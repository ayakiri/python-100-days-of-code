from turtle import Turtle

SNAKE_STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_RANGE = 20


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in SNAKE_STARTING_POS:
            self.add_body_segment(position)

    def add_body_segment(self, position):
        body_segment = Turtle(shape="square")
        body_segment.penup()
        body_segment.color("white")
        body_segment.goto(position)
        self.snake_body.append(body_segment)

    def extend_snake(self):
        self.add_body_segment(self.snake_body[-1].position())

    def move_snake(self):
        for body_segment_num in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[body_segment_num].goto(self.snake_body[body_segment_num - 1].pos())
        self.head.forward(MOVE_RANGE)

    def reset(self):
        for segment in self.snake_body:
            segment.goto(1100, 1100)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
