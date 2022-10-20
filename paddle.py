from turtle import Turtle, Screen

UP = 180
DOWN = 0


class Paddle:
    def __init__(self):
        self.paddle = None

    def create_paddle(self):
        new_paddle = Turtle("square")  # starts with 20 x 20 pixels
        new_paddle.color("white")
        new_paddle.penup()
        new_paddle.turtlesize(stretch_wid=5, stretch_len=1)
        new_paddle.goto(350, 0)
        self.paddle = new_paddle

    def up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)
