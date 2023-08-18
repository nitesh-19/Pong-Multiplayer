import time
from turtle import Screen
from paddle import Paddle
from ball import Ball

SCREEN_WIDTH = 1900
SCREEN_HEIGHT = 1000

screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
paddle1 = Paddle()
paddle1.setposition(SCREEN_WIDTH / 2 - 20, 0)
paddle2 = Paddle()
paddle2.setposition(-SCREEN_WIDTH / 2 + 20, 0)
ball = Ball()
screen.update()
screen.listen()
game_on = True
while game_on:
    screen.onkeypress(fun=paddle1.move_up, key="Up")
    screen.update()
    screen.onkeypress(fun=paddle2.move_up, key="w")
    screen.update()
    screen.onkeypress(fun=paddle1.move_down, key="Down")
    screen.update()
    screen.onkeypress(fun=paddle2.move_down, key="s")

    if paddle2.distance(ball) <= 70 or paddle1.distance(ball) <= 70:
        ball.rebound_in_width()
    screen.update()
    if ball.ycor() >= 450 or ball.ycor() <= -450:
        ball.rebound_in_height()
    screen.onkeypress(fun=ball.rebound_in_width, key="k")
    screen.onkeypress(fun=ball.rebound_in_height, key="j")
    ball.move()
    screen.update()

screen.exitonclick()
