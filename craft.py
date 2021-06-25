from turtle import Turtle

STARTING_X = 0
STARTING_Y = -220


class Craft(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(1, 4)
        self.death_colors = ["gray40", "gray30", "gray20", "gray10", "navy"]
        self.game_start()

    def game_start(self):
        self.goto(STARTING_X, STARTING_Y)
        self.color("black", "gray60")

    def move_left(self):
        if self.xcor() > -330:
            self.goto(self.xcor() - 20, STARTING_Y)

    def move_right(self):
        if self.xcor() < 330:
            self.goto(self.xcor() + 20, STARTING_Y)
