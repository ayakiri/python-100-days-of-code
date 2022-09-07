from turtle import Screen, Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")

        self.pace = 0.05
        self.x_movement = 10
        self.y_movement = 10

    def move(self):
        new_x = self.xcor() + self.x_movement
        new_y = self.ycor() + self.y_movement
        self.goto(new_x, new_y)

    def bounce_on_wall(self):
        self.y_movement *= -1

    def bounce_on_paddle(self):
        self.pace *= 0.9
        self.x_movement *= -1
        self.y_movement += -1

    def reset(self):
        self.x_movement *= -1
        self.pace = 0.1
        self.goto(0, 0)
