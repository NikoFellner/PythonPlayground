from turtle import Turtle, Screen

def movement_forward():
    timmy.forward(10)


def movement_right():
    timmy.right(10)


def movement_left():
    timmy.left(10)


def movement_back():
    timmy.back(10)


timmy = Turtle()
my_screen = Screen()
my_screen.onkeypress(movement_forward, "w")
my_screen.onkeypress(movement_right, "d")
my_screen.onkeypress(movement_left, "a")
my_screen.onkeypress(movement_back, "s")
my_screen.onkey(my_screen.resetscreen, "c")
my_screen.listen()
my_screen.exitonclick()