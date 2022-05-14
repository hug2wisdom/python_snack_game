from tkinter import LEFT
from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
FORWARD_DISTANCE = 20
LEFT = 180
UP = 90
RIGHT = 0
DOWN = 270

class Snack():
    def __init__(self):
        self.snack_list = []
        self.make_snack()
        self.head = self.snack_list[0]
    def make_snack(self):
        for position in POSITIONS:
            new_snack = Turtle("square")
            new_snack.color("white")
            new_snack.penup()
            new_snack.goto(position)
            self.snack_list.append(new_snack)

    def move(self):
        for snack_num in range(len(self.snack_list)-1, 0, -1):
            new_x = self.snack_list[snack_num-1].xcor()
            new_y = self.snack_list[snack_num-1].ycor()
            self.snack_list[snack_num].goto(new_x, new_y)

        self.head.forward(FORWARD_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

