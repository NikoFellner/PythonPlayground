from turtle import Turtle
import random
START_POSITION = (0, 0)
BEGINNING_SPEED = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed_ball = BEGINNING_SPEED
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.speed("fastest")
        self.setheading(random.randint(5, 20))

    def move(self):
        self.forward(self.speed_ball)

    def bounce(self):

        if (self.heading() > 180) and (self.heading() < 360):
            self.setheading(540 - self.heading())

        elif (self.heading() < 180) and (self.heading() > 0):
            self.setheading(180 - self.heading())

    def bounce_wall(self):
        self.setheading(360 - self.heading())

    def reset_ball(self):
        self.goto(START_POSITION)
        self.speed_ball = BEGINNING_SPEED
        self.setheading(random.randint(10, 30))

    def increase_speed(self):
        self.speed_ball += random.randint(1, 5)