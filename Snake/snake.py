from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for positions in STARTING_POSITION:
            self.add_segment(positions)

    def move(self):
        length_snake = len(self.snake_segments) - 1
        for snake_segments in range(length_snake, 0, -1):
            if snake_segments > 0:
                self.snake_segments[snake_segments].goto(self.snake_segments[snake_segments - 1].pos())
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.snake_segments:
            seg.goto(1000, 1000)
        self.snake_segments.clear()
        self.create_snake()
        self.head = self.snake_segments[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def add_segment(self, position):
        new_snake_segment = Turtle()
        new_snake_segment.shape("square")
        new_snake_segment.color("white")
        new_snake_segment.penup()
        new_snake_segment.goto(position)
        self.snake_segments.append(new_snake_segment)

    def extend(self):
        self.add_segment(self.snake_segments[-1].position())