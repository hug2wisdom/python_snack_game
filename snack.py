from turtle import Turtle
POSITIONS = {(0, 0), (-20, 0), (-40, 0)}


class Snack():
    def __init__(self):
        self.snack_list = []
        self.make_snack()

    def make_snack(self):
        for position in POSITIONS:
            new_snack = Turtle("square")
            new_snack.color("white")
            new_snack.goto(position)
            self.snack_list.append(new_snack)
