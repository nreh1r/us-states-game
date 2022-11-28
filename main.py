import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
state_writer = turtle.Turtle()
state_writer.hideturtle()
state_writer.penup()
state_writer.speed("fastest")
states_data = pandas.read_csv("50_states.csv")
states_names = states_data["state"].to_list()


correct_answers = []
game_is_on = True
while game_is_on:
    answer = screen.textinput(title=f"{len(correct_answers)}/50 States Correct",
                              prompt="What's another state's name?").title()

    if answer == "Exit":
        missed_states = []
        for state in states_names:
            if state not in correct_answers:
                missed_states.append(state)
        states_dict = {
            "states": missed_states
        }
        states_df = pandas.DataFrame(states_dict)
        states_df.to_csv("states_to_learn.csv")
        break

    if answer in states_names and answer not in correct_answers:
        state_info = states_data[states_data["state"] == answer]
        position = (int(state_info.x), int(state_info.y))
        print(position)
        state_writer.goto(position)
        state_writer.write(state_info.state.item())
        correct_answers.append(answer)

    if len(correct_answers) == 50:
        state_writer.goto(0, 0)
        state_writer.write("YOU GOT THEM ALL!")
        game_is_on = False
