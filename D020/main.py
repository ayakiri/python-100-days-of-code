from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time


def prepare_screen():
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)


game_is_on = True
screen = Screen()
prepare_screen()

snake = Snake()
food = Food()
scoreboard = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # eat food
    if snake.head.distance(food) < 18:
        food.generate_food()
        snake.extend_snake()
        scoreboard.increase_score()

    # hit the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # hit tail
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
