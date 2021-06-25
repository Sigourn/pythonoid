from turtle import Turtle, Screen
from craft import Craft
from ball import Ball
from brick import Brick
from playsound import playsound
import time

# SCREEN SETUP

screen = Screen()
screen.title("Pythonoid")
screen.setup(width=780, height=600)
screen.bgcolor("navy")
screen.tracer(0)

# BRICKS SETUP

brick_wall = []
brick = Brick()
brick.make_brick_wall(brick_wall)

# CRAFT AND BALL SETUP

craft = Craft()
ball = Ball(craft.xcor())

# PLAYER CONTROLS

screen.listen()

screen.onkeypress(craft.move_left, "Left")
screen.onkeypress(craft.move_right, "Right")
screen.onkey(ball.fire_ball, "space")

# GAMEPLAY

player_lives = 3

game_is_on = True

while game_is_on:
    time.sleep(0.01)
    screen.update()

    # GAME START SETUP
    # If the ball has not been fired yet, then as the player moves the craft the ball (sitting on top of it)
    # will follow along in its movement. If the ball is fired, the ball will start moving on its own.

    if ball.fired is False:
        ball.game_start(craft.xcor())
    else:
        ball.move()

        # WALL COLLISION
        # Checks for collision with the left wall, right wall, and ceiling.

        if ball.xcor() >= 370:
            ball.bounce_left()
        if ball.xcor() <= -380:
            ball.bounce_right()
        if ball.ycor() >= 285:
            ball.bounce_down()

        # BRICK COLLISION
        # Checks collision with bricks, from top to bottom, left to right.
        # If collision is detected with a brick, the brick loses a "life" and is evaluated for removal.

        # There's a specific bug that arises because the bricks are evaluated from left to right, top to bottom.
        # This can cause a brick to be destroyed when the ball should have destroyed the brick beside it or the
        # brick below it.
        # This happens when the ball travels up and left. In this case, we want to reverse evaluation,
        # i.e. reverse the list.

        for brick in brick_wall:

            # BRICK LEFT SIDE COLLISION

            if ball.moving_right() and brick.xcor() - 40 <= ball.xcor() <= brick.xcor() - 30 \
                    and brick.ycor() - 10 <= ball.ycor() <= brick.ycor() + 10:
                ball.bounce_left()
                ball.bounce_down()
                brick.lose_life(brick_wall)
                break

            # BRICK RIGHT SIDE COLLISION

            elif ball.moving_left() and brick.xcor() + 30 <= ball.xcor() <= brick.xcor() + 40 \
                    and brick.ycor() - 10 <= ball.ycor() <= brick.ycor() + 10:
                ball.bounce_right()
                ball.bounce_down()
                brick.lose_life(brick_wall)
                break

            # BRICK BOTTOM SIDE COLLISION

            elif ball.moving_up() and brick.ycor() - 20 <= ball.ycor() <= brick.ycor() - 10 \
                    and brick.xcor() - 40 <= ball.xcor() <= brick.xcor() + 40:
                ball.bounce_down()
                brick.lose_life(brick_wall)
                break

            # BRICK TOP SIDE COLLISION

            elif ball.moving_down() and brick.ycor() + 20 >= ball.ycor() >= brick.ycor() + 10 \
                    and brick.xcor() - 40 <= ball.xcor() <= brick.xcor() + 40:
                ball.bounce_up()
                brick.lose_life(brick_wall)
                break

        # CRAFT COLLISION
        # First it checks that the ball has fired, as to not play the bounce sound when the ball
        # is attached to the craft at the beginning of the game.
        # By checking for ball.y_movement < 0, we ensure that the ball is going down as to not play the
        # bouncing sound while the ball is going up.
        # We ensure that the ball is in the appropriate "collision range" with the craft.
        # We pass the craft's coordinates and the ball's distance to the craft to determine the
        # "ball changes angle" mechanics.

        if ball.fired and ball.moving_down() and -200 >= ball.ycor() >= -230 and \
                craft.xcor() - 50 <= ball.xcor() <= craft.xcor() + 50:
            ball.bounce_craft(craft.xcor(), craft.ycor(), ball.distance(craft))
            playsound("SFX/Arkanoid_Bounce.wav", False)

        # LIFE LOST
        # If the ball goes out of bounds, then the player loses a life.

        if ball.ycor() <= -320:
            playsound("SFX/Arkanoid_Death.wav", False)
            player_lives -= 1

            # DEATH ANIMATION
            # Basic "fade out" animation for the craft, going through a list of progressively darker
            # shades of gray.

            for color in craft.death_colors:
                craft.color(color)
                screen.update()
                time.sleep(0.2)

            # If the player has lives remaining, the craft and the ball are reset to their starting conditions.

            if player_lives > 0:
                time.sleep(2)
                craft.game_start()
                ball.game_start(craft.xcor())

        # GAME WON CONDITION
        # No bricks or life remaining trigger game over.
        # We call one final screen update in case the player has won, so the brick disappears before freezing
        # the screen.

        if len(brick_wall) < 1 or player_lives < 1:
            screen.update()
            game_is_on = False
            time.sleep(2)

# GAME OVER SCREEN
# The screen is cleared, a black screen is created and a message is printed.

screen.clear()
screen.bgcolor("black")
screen.tracer(0)
game_over_message = Turtle()
game_over_message.penup()
game_over_message.hideturtle()
game_over_message.color("white")
game_over_message.write(arg="GAME OVER", align="center", font=("Batang", 20, "normal"))
screen.update()
if player_lives < 1:
    playsound("SFX/Arkanoid_Game_Over.wav", False)

screen.exitonclick()
