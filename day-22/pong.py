import time
from turtle import Screen

from paddle import Paddle
from score import Score
from ball import Ball

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

LEFT_BORDER = -SCREEN_WIDTH / 2 + 50
RIGHT_BORDER = SCREEN_WIDTH / 2 - 50
BOTTOM_BORDER = -SCREEN_HEIGHT / 2 + 20
TOP_BORDER = SCREEN_HEIGHT / 2 - 20

TARGET_SCORE = 10

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong!")

player_1 = Paddle(side="left", canvas_width=SCREEN_WIDTH, canvas_height=SCREEN_HEIGHT)
screen.update()
player_2 = Paddle(side="right", canvas_width=SCREEN_WIDTH, canvas_height=SCREEN_HEIGHT)
screen.update()

ball = Ball()

scoreboard = Score(screen_height=SCREEN_HEIGHT)

screen.listen()
screen.onkey(fun=player_1.up, key="w")
screen.onkey(fun=player_1.down, key="s")
screen.onkey(fun=player_2.up, key="Up")
screen.onkey(fun=player_2.down, key="Down")

game_over = False
while not game_over:
    ball.move()
    screen.update()
    time.sleep(0.1)

    # check for contact with paddle
    if (ball.distance(player_1) < 50 and ball.xcor() < LEFT_BORDER) or (ball.distance(player_2) < 50 and ball.xcor() > RIGHT_BORDER):
        ball.bounce_paddle()
    # check for contact with top/bottom wall
    elif ball.ycor() > TOP_BORDER or ball.ycor() < BOTTOM_BORDER:
        ball.bounce_wall()
    # check if Player 1 missed the ball
    elif ball.xcor() < LEFT_BORDER:
        scoreboard.add_point(2)
        if scoreboard.player_2 == TARGET_SCORE:
            game_over = True
        else:
            ball.reset_ball(2)
    # check if Player 2 missed the ball
    elif ball.xcor() > RIGHT_BORDER:
        scoreboard.add_point(1)
        if scoreboard.player_1 == TARGET_SCORE:
            game_over = True
        else:
            ball.reset_ball(1)

ball.all_done()
player_1.all_done()
player_2.all_done()
scoreboard.game_over()



screen.exitonclick()
