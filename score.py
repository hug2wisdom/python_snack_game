from doctest import FAIL_FAST
from pickle import FALSE
from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.refresh()

    def refresh(self):
        self.goto(0, 270)
        self.write(f"SCORE: {self.score}", FALSE, "center", ("Arial", 18, "bold"))
    
    def increase_score(self):
        self.clear()
        self.score += 1
        self.refresh()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", FALSE, "center", ("Arial", 18, "bold"))