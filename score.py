from turtle import Turtle


class Score(Turtle):
    def __init__(self, destination):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(destination)
        self.score = 0
        self.write(self.score, align="center", font=("Arial", 80, "bold"))

    def add_to_score(self):
        self.clear()
        self.score += 1
        self.write(self.score, align="center", font=("Arial", 80, "bold"))
