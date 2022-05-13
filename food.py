from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.make_foods()
    
    def make_foods(self):
        self.shape("circle")
        self.color("blue")
