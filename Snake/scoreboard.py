from turtle import Turtle
ALIGNMENT = "center"
FONT =("Courier", 12, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.import_high_score()
        self.hideturtle()
        self.speed("fastest")
        self.pencolor("white")
        self.penup()
        self.goto(0, 280)
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_new_high_score()
        self.score = 0
        self.update_scoreboard()

    def import_high_score(self):
        with open(file="data.txt", mode="r") as file:
            all_over_high_score = int(file.read())
        self.high_score = all_over_high_score

    def write_new_high_score(self):
        with open(file="data.txt", mode="w") as file:
            file.write(f"{self.score}")

    #def game_over(self):
    #    self.goto(0, 0)
    #    self.pendown()
    #    self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)
