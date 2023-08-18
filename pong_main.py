import time
from turtle import Screen
from paddle import Paddle

SCREEN_WIDTH = 1900
SCREEN_HEIGHT = 1000

screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
paddle1 = Paddle()
paddle1.setposition(SCREEN_WIDTH / 2 - 20, 0)
paddle2 = Paddle()
paddle2.setposition(-SCREEN_WIDTH / 2 + 20, 0)
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
    screen.update()

screen.exitonclick()
