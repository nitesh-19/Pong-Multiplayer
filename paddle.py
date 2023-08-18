from turtle import Turtle

PADDLE_COLOR = "white"
PADDLE_WIDTH = 5


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(PADDLE_COLOR)
        self.shapesize(stretch_len=PADDLE_WIDTH, stretch_wid=1)
        self.setheading(90)

    def move_up(self):
        self.forward(30)

    def move_down(self):
        self.backward(30)
