from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.pad_1_score = 0
        self.pad_2_score = 0
        self.update_score()

    def update_score(self):
         self.clear()
         self.goto(-100, 200)
         self.write(self.pad_1_score, align="center", font=("Courier", 50, "normal"))
         self.goto(100, 200)
         self.write(self.pad_2_score, align="center", font=("Courier", 50, "normal"))

    def pad_2_point(self):
        self.pad_1_score += 1
        self.update_score()

    def pad_1_point(self):

        self.pad_2_score += 1
        self.update_score()