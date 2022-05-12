from ctypes.wintypes import SC_HANDLE
import time
from turtle import Turtle, Screen

screen = Screen()
# 关闭自动刷新页面
screen.tracer(0)
screen.bgcolor("black")
screen.title("snack game")
screen.setup(width=600, height=600)
positions = [(0, 0), (-20, 0), (-40, 0)]
snack_lists = []
for position in positions:
    snack = Turtle(shape="square")
    snack.color("white")
    snack.penup()
    snack.goto(position)
    snack_lists.append(snack)

game_is_on=True
while game_is_on:
    # 等待方块都走完 再刷新界面
    screen.update()
    for snack in snack_lists:
        snack.forward(40)
        time.sleep(0.5)

screen.exitonclick()
