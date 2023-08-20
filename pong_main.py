import time
from paddle import Paddle
from ball import Ball
from main_screen import MainScreen
from scoreboard import Scoreboard
from Settings import *

screen = MainScreen(SCREEN_WIDTH=SCREEN_WIDTH, SCREEN_HEIGHT=SCREEN_HEIGHT)
paddle1 = Paddle()
paddle1.setposition(SCREEN_WIDTH / 2 - 26, 0)
paddle2 = Paddle()
paddle2.setposition(-SCREEN_WIDTH / 2 + 20, 0)
screen.screen.update()
screen.screen.listen()
screen.screen.onkeypress(fun=paddle1.move_up, key="Up")
screen.screen.onkeypress(fun=paddle1.move_down, key="Down")

# Only allow player2 key control when in multiplayer mode
if GAME_MODE == 2:
    screen.screen.onkeypress(fun=paddle2.move_down, key="s")
    screen.screen.onkeypress(fun=paddle2.move_up, key="w")

player_1 = Scoreboard(X_Coor=-SCREEN_WIDTH / 4, Y_Coor=SCREEN_HEIGHT / 2 - 50)
player_2 = Scoreboard(X_Coor=SCREEN_WIDTH / 4, Y_Coor=SCREEN_HEIGHT / 2 - 50)
game_on = True
ball = Ball()

while game_on:
    # Serve ball with a random angle
    ball.move()
    screen.screen.update()
    time.sleep(0.000001)
    if ball.xcor() <= 0:  # If ball is in the left half of the screen, then only process the relevant code to that half

        # Move paddle automatically if game mode is Single Player
        if GAME_MODE == 1:
            paddle2.goto(paddle2.xcor(), ball.ycor())

        # If ball hits paddle, then bounce it back
        if ball.xcor() <= paddle2.xcor() + 25 and paddle2.ycor() + paddle2.paddle_bound >= ball.ycor() >= \
                paddle2.ycor() - paddle2.paddle_bound:
            ball.rebound_in_width()

        # If player misses the ball then increase the rival's score, reset ball position
        if ball.xcor() <= paddle2.xcor() - 3:
            player_2.score_update()
            if player_2.score == SCORE_TO_WIN:
                player_2.write("Player 2 Wins!")
                break
            time.sleep(1)
            ball.go_home()
            ball.direction("r")
            continue
    else:
        # If ball hits paddle, then bounce it back
        if ball.xcor() >= paddle1.xcor() - 25 and paddle1.ycor() + paddle1.paddle_bound >= ball.ycor() >= \
                paddle1.ycor() - paddle1.paddle_bound:
            ball.rebound_in_width()
        # If player misses the ball then increase the rival's score, reset ball position
        if ball.xcor() > paddle1.xcor() + 3:
            player_1.score_update()
            if player_1.score == SCORE_TO_WIN:
                player_1.write("Player 1 Wins!")
                break
            time.sleep(1)
            ball.go_home()
            ball.direction("l")
            continue
    screen.screen.update()

    # If ball hits the ceiling or the floor, bounce it back
    if ball.ycor() > (SCREEN_HEIGHT / 2 - 10) or ball.ycor() < -(SCREEN_HEIGHT / 2 - 15):
        ball.rebound_in_height()

    screen.screen.update()

screen.screen.exitonclick()
