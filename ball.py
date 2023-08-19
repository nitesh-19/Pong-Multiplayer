from turtle import Turtle
from random import randrange

BALL_COLOR = "white"
SCREEN_WIDTH = 1900
SCREEN_HEIGHT = 800
BALL_STEP = 3


class Ball(Turtle):
    def __init__(self, start_side="l"):
        super().__init__()
        self.penup()
        self.color(BALL_COLOR)
        self.shape("circle")
        hypotenuse = ((SCREEN_WIDTH / 2) ** 2 + (SCREEN_HEIGHT / 2) ** 2) ** (1 / 2)
        angle_allowed = int(SCREEN_HEIGHT / 2 / (hypotenuse / 90))
        if start_side == "l":
            self.direction(randrange(180 - angle_allowed, 180 + angle_allowed, 1))
        elif start_side == "r":
            self.direction(randrange(0 - angle_allowed, 0 + angle_allowed, 1))

    def move(self):
        self.forward(BALL_STEP)

    def direction(self, angle):
        self.setheading(to_angle=angle)

    def rebound_in_width(self):
        self.setheading((180 - self.heading()))

    def rebound_in_height(self):
        self.setheading(360 - self.heading())
