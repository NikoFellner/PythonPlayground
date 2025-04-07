from turtle import Turtle

PLAYER_POSITION = 380
PLAYER_ORIENTATION = 90
POSITIONS_P1 = [(-PLAYER_POSITION, -20), (-PLAYER_POSITION, 0), (-PLAYER_POSITION, 20)]
POSITIONS_P2 = [(PLAYER_POSITION, -20), (PLAYER_POSITION, 0), (PLAYER_POSITION, 20)]
PLAYER_SPEED = 15
PC_SPEED = 12


class Player(Turtle):

    def __init__(self, player_number):
        super().__init__()
        self.playernumber = player_number
        self.player = []
        self.paddle()
        self.define_player_location()
        self.middle = self.player[1]

    def paddle(self):
        for _ in range(0, 3):
            new_segment = Turtle()
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.speed("fastest")
            new_segment.setheading(PLAYER_ORIENTATION)
            self.player.append(new_segment)

    def define_player_location(self):
        if self.playernumber == 1:
            for _ in range(0, 3):
                self.player[_].goto(POSITIONS_P1[_])
        elif self.playernumber == 2:
            for _ in range(0, 3):
                self.player[_].goto(POSITIONS_P2[_])

    def up(self):
        if self.middle.ycor() < 270:
            for segments in self.player:
                segments.forward(PLAYER_SPEED)

    def down(self):
        if self.middle.ycor() > -270:
            for segments in self.player:
                segments.forward(-PLAYER_SPEED)

    def pc_move(self, ball_ycoord):
        if (self.middle.ycor() - ball_ycoord) < 0:
            for segments in self.player:
                segments.forward(PC_SPEED)
        else:
            for segments in self.player:
                segments.forward(-PC_SPEED)

    def reset_position(self):

        if self.playernumber == 1:
            for _ in range(0, 3):
                self.player[_].goto(POSITIONS_P1[_])
        elif self.playernumber == 2:
            for _ in range(0, 3):
                self.player[_].goto(POSITIONS_P2[_])