from turtle import Screen
from snack import Snack
from food import Food
import time
#  设置屏幕相关的参数
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("SNACK GAME")

# 设置 snack 的相关信息
snack = Snack()
game_is_on = True
food = Food()

screen.listen()
screen.onkey(snack.up, "Up")
screen.onkey(snack.down, "Down")
screen.onkey(snack.left, "Left")
screen.onkey(snack.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snack.move()
    if snack.head.distance(food) < 15:
        food.refresh_foods()







screen.exitonclick()