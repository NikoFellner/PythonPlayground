from turtle import Turtle
ALIGNMENT = "center"
FONT =("Courier", 16, "normal")
STROKE_LENGTH = 17
SCORE_POSITIONS = [(-40, 270), (40, 270)]


class Middleline(Turtle):

    def __init__(self):
        super().__init__()
        middle_line = Turtle()
        middle_line.pencolor("white")
        middle_line.setheading(90)
        middle_line.penup()
        middle_line.goto(0, -300)
        middle_line.pendown()
        middle_line.hideturtle()
        while middle_line.ycor() < 320:
            middle_line.forward(STROKE_LENGTH)
            middle_line.penup()
            middle_line.forward(STROKE_LENGTH)
            middle_line.pendown()


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_P1 = 0
        self.score_P2 = 0
        self.hideturtle()
        self.speed("fastest")
        self.pencolor("white")
        self.penup()
        self.initialize_score()

    def initialize_score(self):
        self.goto(SCORE_POSITIONS[0])
        self.write(f"{self.score_P1}", move=False, align=ALIGNMENT, font=FONT)
        self.goto(SCORE_POSITIONS[1])
        self.write(f"{self.score_P2}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self, xcor_ball):
        if xcor_ball < 0:
            self.score_P2 += 1
        elif xcor_ball > 0:
            self.score_P1 += 1
        self.clear()
        self.initialize_score()

    def game_ends(self):
        self.goto(0, 0)
        self.pendown()
        if self.score_P1 > self.score_P2:
            self.write(f"GAME OVER - PLAYER1 Won", move=False, align=ALIGNMENT, font=FONT)
        else:
            self.write(f"GAME OVER - PLAYER1 Won", move=False, align=ALIGNMENT, font=FONT)
