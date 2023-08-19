import time
from turtle import Screen
from paddle import Paddle
from ball import Ball

SCREEN_WIDTH = 1900
SCREEN_HEIGHT = 800

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
paddle1 = Paddle()
paddle1.setposition(SCREEN_WIDTH / 2 - 20, 0)
paddle2 = Paddle()
paddle2.setposition(-SCREEN_WIDTH / 2 + 20, 0)
ball = Ball()
screen.update()
screen.listen()
# screen.tracer(0)

game_on = True
while game_on:

    ball.move()

    screen.update()
    screen.onkeypress(fun=paddle2.move_up, key="w")
    screen.onkeypress(fun=paddle2.move_down, key="s")
    screen.onkeypress(fun=paddle1.move_up, key="Up")
    screen.onkeypress(fun=paddle1.move_down, key="Down")
    screen.update()

    time.sleep(0.0000001)
    if ball.xcor() >= paddle1.xcor() - 20 and paddle1.ycor() + paddle1.paddle_width * 12.5 >= ball.ycor() and paddle1.ycor() - paddle1.paddle_width * 12.5 <= ball.ycor():
        ball.rebound_in_width()
    if ball.xcor() <= paddle2.xcor() + 20 and paddle2.ycor() + paddle2.paddle_width * 12.5 >= ball.ycor() and paddle1.ycor() - paddle1.paddle_width * 12.5 <= ball.ycor():
        ball.rebound_in_width()
    if ball.xcor() > paddle1.xcor() + 10 or ball.xcor() <= paddle2.xcor() - 20:
        break
    screen.update()
    if ball.ycor() > SCREEN_HEIGHT / 2 - 10 or ball.ycor() < -(SCREEN_HEIGHT / 2 - 10):
        ball.rebound_in_height()

screen.update()

screen.exitonclick()
