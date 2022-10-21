from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()

    def movement(self):
        new_x = self.xcor() + 0.75
        new_y = self.ycor() + 0.75
        self.goto(new_x, new_y)
