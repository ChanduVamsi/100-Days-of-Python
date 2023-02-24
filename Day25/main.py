import turtle
import os, pandas

path_to_file = os.path.join(os.path.dirname(__file__), 'blank_states_img.gif')

screen = turtle.Screen()
screen.title("U.S. States Game")
image = path_to_file
screen.addshape(image)
turtle.shape(image)

path_to_file = os.path.join(os.path.dirname(__file__), "50_states.csv")

data = pandas.read_csv(path_to_file)
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").capitalize()
    if answer_state == "Exit":
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)