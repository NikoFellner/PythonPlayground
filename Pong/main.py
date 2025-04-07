from turtle import Screen
from player import Player
from ball import Ball
from scoreboard import Scoreboard, Middleline
import time
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
POINTS_FOR_WIN = 10


def initialize_screen():
    my_screen.bgcolor("black")
    my_screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    my_screen.listen()
    my_screen.tracer(0)
    my_screen.title("PONG")


game_is_on = True
my_screen = Screen()

initialize_screen()

player1 = Player(1)
player2 = Player(2)
ball = Ball()
scoreboard = Scoreboard()
middle_line = Middleline()

my_screen.onkeypress(player1.up, "Up")
my_screen.onkeypress(player1.down, "Down")
# my_screen.onkeypress(player2.up, "w")
# my_screen.onkeypress(player2.down, "s")

while game_is_on:
    my_screen.update()
    time.sleep(0.15)
    ball.move()
    # if it is want to play against Computer
    if player2.middle.ycor() != ball.ycor():
        player2.pc_move(ball_ycoord=ball.ycor())
    # Bounce ball ob paddle
    if ball.distance(player2.middle.position()) < 25 or ball.distance(player1.middle.position()) < 25:
        ball.bounce()
        ball.increase_speed()
    # Bounce ball on upper and lower walls
    if ball.ycor() < -SCREEN_HEIGHT/2 + 20 or ball.ycor() > SCREEN_HEIGHT/2 - 20:
        ball.bounce_wall()
    # if player got one point
    if ball.xcor() > SCREEN_WIDTH/2 or ball.xcor() < -SCREEN_WIDTH/2:
        scoreboard.increase_score(xcor_ball=ball.xcor())
        ball.reset_ball()
        player1.reset_position()
        player2.reset_position()
        time.sleep(1)
    # Game Ends when the first player reaches amount of Points
    if scoreboard.score_P1 == POINTS_FOR_WIN or scoreboard.score_P2 == POINTS_FOR_WIN:
        game_is_on = False
        scoreboard.game_ends()


my_screen.exitonclick()
