from turtle import Screen, Turtle
from Settings import *

def draw_centerline(SCREEN_HEIGHT):
    """
    Draws a dotted line across the center of the screen

    :param SCREEN_HEIGHT: Height of the screen in Pixels
    :return: None
    """
    pen = Turtle()
    pen.color(CENTERLINE_COLOR)
    pen.penup()
    pen.goto(0, -SCREEN_HEIGHT)
    pen.setheading(90)
    for y in range(SCREEN_HEIGHT, -SCREEN_HEIGHT, -40):
        pen.goto(0, y)
        pen.pendown()
        pen.forward(20)
        pen.penup()
        pen.forward(20)


class MainScreen:

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        """
        Initializes the background for the game

        :param SCREEN_WIDTH:
        :param SCREEN_HEIGHT:
        """
        self.screen = Screen()
        self.screen.SCREEN_WIDTH = SCREEN_WIDTH
        self.screen.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.screen.tracer(0)
        self.is_paused = 0
        self.screen.bgcolor(BG_COLOR)
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        draw_centerline(SCREEN_HEIGHT)
