from turtle import Screen

from paddle import Paddle
from score import Score
from ball import Ball

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong!")

player_1 = Paddle(side="left",canvas_width=SCREEN_WIDTH)
player_2 = Paddle(side="right",canvas_width=SCREEN_WIDTH)



screen.listen()
screen.onkey(fun=player_1.up, key="w")
screen.onkey(fun=player_1.down, key="s")
screen.onkey(fun=player_2.up, key="Up")
screen.onkey(fun=player_2.down, key="Down")

game_over = False
while not game_over:
    screen.update()







screen.exitonclick()
