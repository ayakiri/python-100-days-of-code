from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# prepare screen
screen = Screen()
screen.title("Ping pong")
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.tracer(0)
game_is_on = True

right_paddle = Paddle("right")
left_paddle = Paddle("left")

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.move_up, "k")
screen.onkey(right_paddle.move_down, "m")
screen.onkey(left_paddle.move_up, "s")
screen.onkey(left_paddle.move_down, "z")

while game_is_on:
    time.sleep(ball.pace)
    screen.update()
    ball.move()
    scoreboard.update_scoreboard()

    # ball hits wall
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_on_wall()

    # ball hits paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 430) or \
            (ball.distance(left_paddle) < 40 and ball.xcor() > -480):
        ball.bounce_on_paddle()

    # ball misses right paddle
    if ball.xcor() > 500:
        ball.reset()
        scoreboard.left_score += 1

    # ball misses left paddle
    if ball.xcor() < -500:
        ball.reset()
        scoreboard.right_score += 1

screen.exitonclick()
