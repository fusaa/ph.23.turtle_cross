from turtle import Turtle
from random import choice
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
AVAIL_POSITIONS_START_Y = [-250,-200,-150,-100,-50,0,50,100,150,200,250]

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(choice(COLORS))
        self.penup()
        self.goto(270, choice(AVAIL_POSITIONS_START_Y))
        self.left(180)
        self.step = 0
        self.steps = STARTING_MOVE_DISTANCE + self.step

    def move(self):
        self.forward(self.steps)
        self.steps = STARTING_MOVE_DISTANCE + self.step







