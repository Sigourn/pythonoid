from turtle import Turtle
from playsound import playsound


class Brick(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("navy")
        self.shape("square")
        self.shapesize(1, 3, outline=2)
        self.brick_colors = ["gray60", "red", "yellow", "RoyalBlue1", "magenta2", "green3"]
        self.brick_x_position = -360
        self.brick_y_position = 220
        self.lives = 1

    # The navy color makes the initial brick (which isn't part of the wall we will build) blend in
    # with the background. Yay!

    # BRICK WALL
    # We make a brick wall of 6 rows (one per color) and 13 bricks.
    # Each brick is then added to a brick_wall list.

    def make_brick_wall(self, brick_wall):
        for color in self.brick_colors:
            for _ in range(13):
                brick = Brick()
                brick.color("black", color)
                brick.goto(self.brick_x_position, self.brick_y_position)
                self.brick_x_position += 60
                if brick.color() == ("black", "gray60"):
                    brick.lives = 2
                brick_wall.append(brick)
            self.brick_x_position = -360
            self.brick_y_position -= 20

    # LOSE LIFE
    # When a brick is hit, it loses a life. If the brick has less than one life, it is removed.
    # If it has one life remaining, then a different collision sound is played.

    def lose_life(self, brick_wall):
        self.lives -= 1
        if self.lives < 1:
            self.color("navy")
            brick_wall.remove(self)
            playsound("SFX/Arkanoid_Brick.wav", False)
        else:
            playsound("SFX/Arkanoid_Silver_Brick.wav", False)