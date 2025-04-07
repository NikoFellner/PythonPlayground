'''
import colorgram
colors = colorgram.extract("image.jpg", 16)
for color in colors:
    rgb = color.rgb
    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]
    new_color = (red, green, blue)
    color_list.append(new_color)
'''


import random
import turtle

turtle.colormode(255)
color_list = [(197, 165, 119), (144, 81, 56), (220, 201, 138), (61, 95, 121), (165, 150, 54), (136, 162, 180),
              (131, 34, 23), (52, 119, 87), (73, 37, 29), (190, 96, 82), (145, 177, 150), (100, 76, 80)]

timmy = turtle.Turtle()
timmy.penup()
timmy.hideturtle()
timmy.speed("fastest")
timmy.goto(-300.00, -300.00)

for _ in range(10):
    for _ in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.forward(70)
    actual_ycor = timmy.ycor() + 70
    timmy.goto(-300.00, actual_ycor)


my_screen = turtle.Screen()
my_screen.exitonclick()