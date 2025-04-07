import turtle
import pandas

FONT = ("Arial", 10, "normal")


def correct_state():
    data_row = data[data["state"] == states]
    x_cor = int(data_row["x"])
    y_cor = int(data_row["y"])
    state.goto(x_cor, y_cor)
    state.write(states, font=FONT)


screen = turtle.Screen()
screen.title("US-STATE-GAME")
image = "blank_states_img.gif"

state = turtle.Turtle()
state.penup()
state.hideturtle()

screen.addshape(image)
turtle.shape(image)
game_is_on = True
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
correct_states = []
missed_states = []

while game_is_on:
    answer_state = screen.textinput(title=f"{len(correct_states)}/50 States guessed correct",
                                    prompt="Type in another State: ")


    if answer_state == "exit":
        # for every_state in data["state"]:
        #     if every_state.lower() not in correct_states:
        #         missed_states.append(every_state)
        missed_states = [state for state in all_states if state.lower() not in correct_states]
        df = pandas.DataFrame(missed_states)
        df.to_csv("solution.csv")
        game_is_on = False

    else:
        for states in data["state"]:
            if answer_state.lower() == states.lower() and answer_state.lower() not in correct_states:
                correct_state()
                correct_states.append(states.lower())

        if len(correct_states) >= 50:
            state.goto(-100, 0)
            state.write("You got all State, perfect Game!", font=FONT)
            game_is_on = False

screen.exitonclick()
#
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
