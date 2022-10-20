from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("ポン")
screen.tracer(0)

# create 2 paddles
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))


screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_active = True

while game_is_active:
    screen.update()

screen.exitonclick()
