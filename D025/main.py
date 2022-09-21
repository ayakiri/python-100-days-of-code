import turtle
import pandas

FONT = ('Arial', 7, 'normal')

screen = turtle.Screen()
screen.title("US States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

states_data = pandas.read_csv("50_states.csv")
all_states = states_data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/{len(all_states)} States Correct",
                              prompt="What is another state's name?").title()
    if answer == "Exit":
        states_to_learn = []
        for state in all_states:
            if state not in guessed_states:
                states_to_learn.append(state)

        states_to_learn_dict = {"States to learn:": states_to_learn}

        new_csv = pandas.DataFrame(states_to_learn_dict)
        new_csv.to_csv("states_to_learn.csv")
        break
    if answer in all_states and answer not in guessed_states:
        state = states_data[states_data.state == answer]
        guessed_states.append(answer)

        writing_turtle = turtle.Turtle()
        writing_turtle.hideturtle()
        writing_turtle.penup()
        writing_turtle.goto(int(state.x), int(state.y))
        writing_turtle.write(answer, False, font=FONT)

turtle.mainloop()
