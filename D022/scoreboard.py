from turtle import Screen, Turtle

ALIGNMENT = "center"
FONT = ("Courier", 32, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 230)
        self.right_score = 0
        self.left_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.left_score} : {self.right_score}", align=ALIGNMENT, font=FONT)
