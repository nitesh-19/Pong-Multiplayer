from turtle import Screen, Turtle


def draw_centerline(SCREEN_HEIGHT):
    pen = Turtle()
    pen.color("white")
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
        self.screen = Screen()
        self.screen.SCREEN_WIDTH = SCREEN_WIDTH
        self.screen.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.screen.tracer(0)
        self.is_paused = 0
        self.screen.bgcolor("black")
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        draw_centerline(SCREEN_HEIGHT)

