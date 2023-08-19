from turtle import Turtle

PADDLE_COLOR = "white"
PADDLE_WIDTH = 10
PADDLE_STEP = 30


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(PADDLE_COLOR)
        self.paddle_width = PADDLE_WIDTH
        self.shapesize(stretch_len=PADDLE_WIDTH, stretch_wid=1)
        self.setheading(90)

    def move_up(self):
        self.forward(PADDLE_STEP)

    def move_down(self):
        self.backward(PADDLE_STEP)
