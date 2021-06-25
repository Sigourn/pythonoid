from turtle import Turtle
from playsound import playsound

X_MOVEMENT = 5
Y_MOVEMENT = 5


class Ball(Turtle):

    def __init__(self, craft_xcor):
        super().__init__()
        self.shape("circle")
        self.color("black", "white")
        self.penup()
        self.fired = False
        self.x_movement = X_MOVEMENT
        self.y_movement = Y_MOVEMENT
        self.starting_y = -200
        self.game_start(craft_xcor)

    # MAKES THE BALL FOLLOW THE CRAFT AT THE BEGINNING OF THE GAME

    def game_start(self, craft_xcor):
        self.goto(craft_xcor + 10, self.starting_y)
        self.x_movement = X_MOVEMENT
        self.y_movement = Y_MOVEMENT
        self.fired = False

    # TRIGGERED BY PLAYER INPUT. THE BALL IS FIRED AND CAN NOW BEGIN TO MOVE

    def fire_ball(self):
        if not self.fired:
            self.fired = True
            playsound("SFX/Arkanoid_Bounce.wav", False)

    # BALL MOVEMENT

    def move(self):
        self.goto(self.xcor() + self.x_movement, self.ycor() + self.y_movement)

    # BOUNCE AFTER COLLISION WITH WALLS, CEILING, OR BRICKS

    def bounce_left(self):
        if self.x_movement > 0:
            self.x_movement *= -1

    def bounce_right(self):
        if self.x_movement < 0:
            self.x_movement *= -1

    def bounce_down(self):
        if self.y_movement > 0:
            self.y_movement *= -1

    def bounce_up(self):
        if self.y_movement < 0:
            self.y_movement *= -1

    # BOUNCE AFTER COLLISION WITH CRAFT

    def bounce_craft(self, craft_xcor, craft_ycor, distance_to_craft):
        if distance_to_craft >= 20:

            # The closer the ball is to one of the ends of the craft, the more pronounced its angle will be.

            if distance_to_craft >= 35:
                self.x_movement = 10
                self.y_movement = 2.5
            elif distance_to_craft >= 30:
                self.x_movement = 8
                self.y_movement = 3.5
            else:
                self.x_movement = 6
                self.y_movement = 4.5

            # Switches the direction of the ball on the X axis depending on how close to each end of the craft
            # the ball is.

            if self.x_movement > 0 and self.xcor() < craft_xcor:
                self.bounce_left()
            elif self.x_movement < 0 and self.xcor() > craft_xcor:
                self.bounce_right()
        else:
            self.x_movement = 5
            self.y_movement = 5

    # These functions determine what direction the ball is moving in.

    def moving_right(self):
        if self.x_movement > 0:
            return True
        return False

    def moving_left(self):
        if self.x_movement < 0:
            return True
        return False

    def moving_up(self):
        if self.y_movement > 0:
            return True
        return False

    def moving_down(self):
        if self.y_movement < 0:
            return True
        return False
