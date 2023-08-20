from turtle import Turtle
from Settings import *


class Scoreboard:
    def __init__(self, X_Coor, Y_Coor):
        self.score_writer = Turtle()
        self.score_writer.hideturtle()
        self.score_writer.penup()
        self.score = 0
        self.score_writer.color(SCORE_COLOR)
        self.score_writer.goto(X_Coor, Y_Coor)
        self.score_writer.pendown()

        self.score_writer.write(str(self.score), align="center", font=('Arial', 30, 'bold'))

    def score_update(self):
        self.score += 1
        self.score_writer.clear()
        self.score_writer.write(str(self.score), align="center", font=('Arial', 30, 'bold'))

    def write(self, message):
        self.score_writer.color("green")
        self.score_writer.goto(0, 0)
        self.score_writer.write(message, align="center", font=('Arial', 30, 'bold'))
