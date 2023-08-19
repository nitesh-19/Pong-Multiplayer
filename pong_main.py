import time
from paddle import Paddle
from ball import Ball
from main_screen import MainScreen

SCREEN_WIDTH = 1900
SCREEN_HEIGHT = 800

screen = MainScreen(SCREEN_WIDTH=SCREEN_WIDTH, SCREEN_HEIGHT=SCREEN_HEIGHT)
paddle1 = Paddle(paddle_width=5)
paddle1.setposition(SCREEN_WIDTH / 2 - 20, 0)
paddle2 = Paddle(paddle_width=4)
paddle2.setposition(-SCREEN_WIDTH / 2 + 20, 0)
ball = Ball()
screen.screen.update()
screen.screen.listen()
screen.screen.onkeypress(fun=paddle1.move_up, key="Up")
screen.screen.onkeypress(fun=paddle1.move_down, key="Down")
screen.screen.onkeypress(fun=paddle2.move_down, key="s")
screen.screen.onkeypress(fun=paddle2.move_up, key="w")
game_on = True
while game_on:
    ball.move()
    screen.screen.update()
    screen.screen.update()
    time.sleep(0.0000001)
    if ball.xcor() <= 0:  # If ball is in the left half of the screen, then only process the relevant code to that half
        if ball.xcor() <= paddle2.xcor() + 25 and paddle2.ycor() + paddle2.paddle_bound >= ball.ycor() >= \
                paddle2.ycor() - paddle2.paddle_bound:
            ball.rebound_in_width()
        if ball.xcor() <= paddle2.xcor() - 20:
            break
    else:
        if ball.xcor() >= paddle1.xcor() - 25 and paddle1.ycor() + paddle1.paddle_bound >= ball.ycor() >= \
                paddle1.ycor() - paddle1.paddle_bound:
            ball.rebound_in_width()

        if ball.xcor() > paddle1.xcor() + 10:
            break
    screen.screen.update()
    if ball.ycor() > (SCREEN_HEIGHT / 2 - 10) or ball.ycor() < -(SCREEN_HEIGHT / 2 - 10):
        ball.rebound_in_height()
    screen.screen.update()

screen.screen.exitonclick()
