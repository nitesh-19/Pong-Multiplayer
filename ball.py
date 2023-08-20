from turtle import Turtle
from random import randrange, randint
from Settings import *


class Ball(Turtle):
    def __init__(self):
        """
        Creates a ball object
        """
        super().__init__()
        self.penup()
        self.color(BALL_COLOR)
        self.shape("circle")
        hypotenuse = ((((SCREEN_WIDTH / 2) ** 2) + ((SCREEN_HEIGHT / 2) ** 2)) ** 0.5)
        self.restricted_area = 10  # Restricted angle from x-axis

        # Angle through which the ball is allowed to be served
        self.angle_allowed = int(SCREEN_HEIGHT / 2 / (hypotenuse / 90)) - self.restricted_area - 12
        # List of allowable sectors in all 4 quadrants such that the ball is not served vertically or horizontally, and
        # is always playable by the player
        self.sectors = [(180 - self.restricted_area, 180 - self.restricted_area - self.angle_allowed),
                        (180 + self.restricted_area + self.angle_allowed, 180 + self.restricted_area),
                        (self.restricted_area, self.angle_allowed),
                        (360 - self.restricted_area - self.angle_allowed, 360 - self.restricted_area)]

        self.direction("l")  # Ball is always served to the left paddle when the game starts

    def move(self):
        """
        Move the ball ahead without changing its direction.

        :return:
        """
        self.forward(BALL_STEP)

    def direction(self, start_side):
        """
        Picks a random allowable angle in which the ball will be served in the left or the right direction as supplied
        in the argument

        :param start_side: Takes "l" or "r" as arguments to serve in the direction.
        :return: None
        """
        if start_side == "l":
            random_sector = randint(0, 1)
            self.setheading(randrange(self.sectors[random_sector][1], self.sectors[random_sector][0], 1))
        elif start_side == "r":
            random_sector = randint(2, 3)
            self.setheading(randrange(self.sectors[random_sector][0], self.sectors[random_sector][1], 1))

    def go_home(self):
        """
        Resets the ball position to (0,0)

        :return:
        """
        self.goto(0, 0)

    def rebound_in_width(self):
        """
        Rebound ball if hits a vertical object

        :return:
        """
        self.setheading((180 - self.heading()))
        self.forward(11)

    def rebound_in_height(self):
        """
        Rebound ball if hits a horizontal object

        :return:
        """
        self.setheading(360 - self.heading())
        self.forward(11)
