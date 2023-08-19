from turtle import Turtle

PADDLE_COLOR = "gray"
paddle_width = 2
PADDLE_STEP = 30
SCREEN_WIDTH = 1900
SCREEN_HEIGHT = 800


class Paddle(Turtle):
    def __init__(self, paddle_width):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(PADDLE_COLOR)
        self.shapesize(stretch_len=paddle_width, stretch_wid=1)
        self.setheading(90)
        self.paddle_bound = paddle_width * 12.5

    def move_up(self):
        if self.ycor() + self.paddle_bound >= SCREEN_HEIGHT / 2:
            pass
        else:
            self.forward(PADDLE_STEP)

    def move_down(self):
        if self.ycor() - self.paddle_bound <= -SCREEN_HEIGHT / 2:
            pass
        else:
            self.backward(PADDLE_STEP)
