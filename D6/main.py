#Escaping the maze by robot from Reeborg:
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def go_right():
    turn_right()
    move()

# find a wall
while front_is_clear():
    move()
# make sure to have a wall at a right side
turn_left()

# follow the right edge of the maze
while not at_goal():
    if not wall_on_right():
        go_right()
    elif not wall_in_front():
        move()
    else:
        turn_left()