from turtle import Screen
from snack import Snack
from food import Food
from score import Scoreboard
from set_difficulty import Setdifficulty
import time
#  设置屏幕相关的参数
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("SNACK GAME")

# 设置 snack 的相关信息
snack = Snack()
food = Food()
scoreboard  = Scoreboard()
set_difficulty = Setdifficulty()
delay_time = set_difficulty.choose()

screen.listen()
screen.onkey(snack.up, "Up")
screen.onkey(snack.down, "Down")
screen.onkey(snack.left, "Left")
screen.onkey(snack.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(delay_time)
    snack.move()
    if snack.head.distance(food) < 15:
        food.refresh_foods()
        scoreboard.increase_score()
        snack.extend_snack()

    if snack.head.xcor() > 280 or snack.head.xcor() < (-280) or snack.head.ycor() > 280 or snack.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    for snack_piece in snack.snack_list[1:]:
         if snack.head.distance(snack_piece) < 10:
             scoreboard.game_over()
             game_is_on = False


screen.exitonclick()