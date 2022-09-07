from turtle import Screen, Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        if position == "right":
            self.goto(450, 0)
        elif position == "left":
            self.goto(-450, 0)

    def move_up(self):
        if self.ycor() < 240:
            new_pos = self.ycor() + 20
            self.goto(self.xcor(), new_pos)

    def move_down(self):
        if self.ycor() > -220:
            new_pos = self.ycor() - 20
            self.goto(self.xcor(), new_pos)
