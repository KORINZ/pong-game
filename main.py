from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("ポン")
screen.tracer(0)

paddle = Paddle()
paddle.create_paddle()

screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")

game_is_active = True

while game_is_active:
    screen.update()

screen.exitonclick()
