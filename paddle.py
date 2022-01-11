from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, destination):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=5)
        self.setheading(90)
        self.goto(destination)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.back(20)
