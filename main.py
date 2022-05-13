from turtle import Screen
from snack import Snack
from food import Food
#  设置屏幕相关的参数
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
# screen.tracer(0)
screen.title("SNACK GAME")

# 设置 snack 的相关信息
snack = Snack()
food = Food()


screen.exitonclick()