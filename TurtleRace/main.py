from turtle import Turtle, Screen
import random


def finish_line():
    finish = Turtle()
    finish.hideturtle()
    finish.penup()
    finish.goto(230, 350)
    finish.pendown()
    finish.goto(230, -350)


def set_new_turtle(turtle_color):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(turtle_color)
    new_turtle.speed(5)
    turtle_list.append(new_turtle)


def move_to_start(turtle_to_move, start_position):
    turtle_to_move.penup()
    turtle_to_move.goto(x=-230, y=start_position)


def random_speed(the_turtle_moving):
    the_turtle_moving.forward(random.randint(1, 10))


def is_turtle_on_finish(the_turtles):
    for turtles in the_turtles:
        if turtles.xcor() >= 230:
            return False
    return True


def winning_color(list_of_turtles, user_guess):
    for turtles in list_of_turtles:
        if turtles.xcor() >= 230:
            winner = turtles.color()

    if user_guess == winner[0]:
        print(f"You won! {winner[0]} reached the Finish first!")
    else:
        print(f"You lose. {winner[0]} reached the Finish first and so before {user_guess}.")
    return


my_screen = Screen()
my_screen.setup(width=600, height=700)
user_bet = my_screen.textinput(title="Make your bet!", prompt="Choose your Color "
                                                              "(red, yellow, blue, green, orange, purple, "
                                                              "cyan, hotpink, sienna1, magenta, NavyBlue): ")
color_list = ["red", "yellow", "blue", "orange", "purple", "green", "cyan", "hotpink", "sienna1", "magenta", "NavyBlue"]
turtle_list = []
Turtle_ycor = -250
race_is_on = True


finish_line()
for colors in color_list:
    set_new_turtle(colors)
    move_to_start(turtle_list[-1], Turtle_ycor)
    Turtle_ycor += 50

while race_is_on:
    for every_turtle in turtle_list:
        random_speed(every_turtle)
    race_is_on = is_turtle_on_finish(turtle_list)

winning_color(turtle_list, user_bet)
my_screen.exitonclick()
