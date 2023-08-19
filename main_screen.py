from turtle import Screen, Turtle


class MainScreen(Screen):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.tracer(0)
        self.bgcolor("black")
        self.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

    def draw_centerline(self):
        pen = Turtle()
        pen.color("white")
        pen.penup()
        pen.goto(0, -self.SCREEN_HEIGHT)
        for y in range(self.SCREEN_HEIGHT, -self.SCREEN_HEIGHT, -40):
            pen.goto(0, y)
            pen.pendown()
            pen.forward(20)
            pen.penup()
            pen.forward(20)
