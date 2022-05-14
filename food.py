from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.make_foods()
    
    def make_foods(self):
        self.shape("circle")
        self.color("blue")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.speed("fastest")
        self.refresh_foods()

    def refresh_foods(self):
        position_x = random.randint(-280, 280)
        position_y = random.randint(-280, 280)
        self.goto(position_x, position_y)