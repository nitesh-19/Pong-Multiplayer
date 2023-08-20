from turtle import Turtle
from random import randrange, randint
from Settings import *


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(BALL_COLOR)
        self.shape("circle")
        hypotenuse = ((((SCREEN_WIDTH / 2) ** 2) + ((SCREEN_HEIGHT / 2) ** 2)) ** 0.5)
        self.restricted_area = 10  # restricted angle from x axis
        self.angle_allowed = int(SCREEN_HEIGHT / 2 / (hypotenuse / 90)) - self.restricted_area - 12
        self.sectors = [(180 - self.restricted_area, 180 - self.restricted_area - self.angle_allowed),
                        (180 + self.restricted_area + self.angle_allowed, 180 + self.restricted_area),
                        (self.restricted_area, self.angle_allowed),
                        (360 - self.restricted_area - self.angle_allowed, 360 - self.restricted_area)]

        self.direction("l")

    def move(self):
        self.forward(BALL_STEP)

    def direction(self, start_side):
        if start_side == "l":
            random_sector = randint(0, 1)
            self.setheading(randrange(self.sectors[random_sector][1], self.sectors[random_sector][0], 1))
        elif start_side == "r":
            random_sector = randint(2, 3)
            self.setheading(randrange(self.sectors[random_sector][0], self.sectors[random_sector][1], 1))

    def go_home(self):
        self.goto(0, 0)

    def rebound_in_width(self):
        self.setheading((180 - self.heading()))
        self.forward(11)

    def rebound_in_height(self):
        self.setheading(360 - self.heading())
        self.forward(11)
