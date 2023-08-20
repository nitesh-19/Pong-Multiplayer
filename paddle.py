from turtle import Turtle
from Settings import *


class Paddle(Turtle):
    def __init__(self, paddle_width=4):
        """
        Creates a paddle of default length 4 if no custom length is supplied.

        :param paddle_width:
        """
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(PADDLE_COLOR)
        self.shapesize(stretch_len=paddle_width, stretch_wid=1)
        self.setheading(90)
        self.paddle_bound = paddle_width * 12.5

    def move_up(self):
        """
        Moves paddle in the upward direction until the screen limit

        :return:
        """
        if self.ycor() + self.paddle_bound >= SCREEN_HEIGHT / 2 + 15:
            pass
        else:
            self.forward(PADDLE_STEP)

    def move_down(self):
        """
        Moves the paddle in the downward direction until the screen limit

        :return:
        """
        if self.ycor() - self.paddle_bound <= -SCREEN_HEIGHT / 2 + 15:
            pass
        else:
            self.backward(PADDLE_STEP)
