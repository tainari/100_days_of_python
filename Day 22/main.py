from turtle import Screen
from net import Net
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
PLAY_UNTIL = 10

#create screen
screen = Screen()
screen.setup(width=WINDOW_WIDTH,height=WINDOW_HEIGHT)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

#create net
net = Net(WINDOW_HEIGHT)

#screate scoreboard
scoreboard = Scoreboard(WINDOW_HEIGHT)

#create left paddle
left_paddle = Paddle(window_width=WINDOW_WIDTH, window_height=WINDOW_HEIGHT, side="left")

#create right paddle
right_paddle = Paddle(window_width=WINDOW_WIDTH, window_height=WINDOW_HEIGHT, side="right")



#create ball
ball = Ball()

#screate scorekeeper

screen.update()

#create keybindings for paddles
screen.listen()
screen.onkey(left_paddle.move_up,'w')
screen.onkey(left_paddle.move_down,'s')
screen.onkey(right_paddle.move_up,'Up')
screen.onkey(right_paddle.move_down,'Down')
# screen.onkey(ball.start_moving," ")

#ball mechanism
playing = True
last_point = "left"
while playing:
    # print(ball.is_moving)
    ball.move_ball(last_point)
    # ball hits top or bottom wall
    if ball.ycor() >= (WINDOW_HEIGHT/2 - 10) or ball.ycor() <= (-WINDOW_HEIGHT/2 + 10):
        ball.bounce()
        # ball hits paddle
    elif (ball.xcor() < (-WINDOW_WIDTH / 2 + 20)
          and
            ball.distance(left_paddle) < 50):
          #left_paddle.ycor() - 50 <= ball.ycor() <= left_paddle.ycor() + 50):  # ball.distance(left_paddle) <= 20:
        ball.bounce_paddle('left')
    elif (ball.xcor() > (WINDOW_WIDTH / 2 - 20)
          and
            ball.distance(right_paddle) < 50 ):
          #right_paddle.ycor() - 50 <= ball.ycor() <= right_paddle.ycor() + 50):  # ball.distance(right_paddle) <= 20:
        ball.bounce_paddle('right')
    #point for right paddle
    elif ball.xcor() <= -WINDOW_WIDTH/2:
        scoreboard.increase_score('right')
        last_point = "right"
        ball.bounce_paddle()
        ball.reset_ball()
    #point for left paddle
    elif ball.xcor() >= WINDOW_WIDTH / 2:
        scoreboard.increase_score('left')
        last_point = "left"
        ball.bounce_paddle()
        ball.reset_ball()
    if scoreboard.max_points >= PLAY_UNTIL:
        playing = False
    screen.update()

ball.hideturtle()
if scoreboard.right_score > scoreboard.left_score:
    scoreboard.game_over("Right player")
else:
    scoreboard.game_over("Left player")

# x = input()
screen.exitonclick()