STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.color("green")
        self.goto(STARTING_POSITION)

    def move_up(self):
        new_y_cor = self.ycor() + MOVE_DISTANCE
        self.sety(new_y_cor)