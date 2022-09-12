from turtle import Turtle

FONT = ("Courier", 24, "normal")
POSITION = (-280, 250)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("grey")
        self.goto(POSITION)
        self.hideturtle()
        self.level = 1

    def write_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
