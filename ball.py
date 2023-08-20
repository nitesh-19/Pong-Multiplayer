from turtle import Turtle
from random import randrange
from Settings import *


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(BALL_COLOR)
        self.shape("circle")
        hypotenuse = ((SCREEN_WIDTH / 2) ** 2 + (SCREEN_HEIGHT / 2) ** 2) ** (1 / 2)
        self.angle_allowed = int(SCREEN_HEIGHT / 2 / (hypotenuse / 90)) - 10
        print(self.angle_allowed)
        self.direction("l")

    def move(self):
        self.forward(BALL_STEP)

    def direction(self, start_side):
        if start_side == "l":
            self.setheading(randrange(160 - self.angle_allowed, 160 + self.angle_allowed, 1))
        elif start_side == "r":
            self.setheading(randrange(20 - self.angle_allowed, 20 + self.angle_allowed, 1))

    def go_home(self):
        self.goto(0, 0)

    def rebound_in_width(self):
        self.setheading((180 - self.heading()))

    def rebound_in_height(self):
        self.setheading(360 - self.heading())
