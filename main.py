from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("ポン")
screen.tracer(0)

# create 2 paddles
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

# create the ball
ball = Ball()

# create the scoreboard
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_active = True
while game_is_active:
    # time.sleep(0.1)
    screen.update()
    ball.movement()

    # wall collision detection
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # paddle collision detection
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # paddle misses detection
    if ball.xcor() > 380:  # right paddle
        ball.reset_position()
        scoreboard.left_point()
    if ball.xcor() < -380:  # left paddle
        ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()
