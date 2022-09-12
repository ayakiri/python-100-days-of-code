import time
from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = Cars()
scoreboard = Scoreboard()
scoreboard.write_score()

screen.listen()
screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()

    # player reaches end
    if player.ycor() > 280:
        player.reset()
        scoreboard.increase_level()
        cars.increase_speed()

    # player collides with car
    for car in cars.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
