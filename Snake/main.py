from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


def starting_screen():
    my_screen.setup(width=600, height=600)
    my_screen.tracer(0)
    my_screen.bgcolor("black")
    my_screen.title("My snake Game")


game_is_on = True
my_screen = Screen()
starting_screen()
snake = Snake()
food = Food()
scoreboard = ScoreBoard()


my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")

while game_is_on:
    my_screen.update()
    time.sleep(0.15)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segments in snake.snake_segments[1:]:
        if snake.head.distance(segments) < 10:
            scoreboard.reset()
            snake.reset()


my_screen.exitonclick()
