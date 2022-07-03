FONT = ("Courier", 24, "normal")
from turtle import  Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.color("blue")
        self.hideturtle()
        self.goto(-200, 250)
        self.write(f" Level : {self.score}", align="center", font=FONT)
    def increase(self):
        self.clear()
        self.score += 1
        self.write(f" Level : {self.score}", align="center", font=FONT)

    def print(self):
        self.goto(0, 0)
        self.write(f" GAME OVER", align="center", font=FONT)