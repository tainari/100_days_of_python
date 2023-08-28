from turtle import Turtle
import random, time

BALL_SPEED = 2

class Ball(Turtle):
    def __init__(self,screen_width = 1000):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.width(10)
        self.up()
        self.is_moving = False
        self.x_move = BALL_SPEED
        self.y_move = BALL_SPEED

    def reset_ball(self):
        self.reset()
        self.shape("circle")
        self.color("white")
        self.width(10)
        self.up()
        self.is_moving = False
    def move_ball(self,last_point="left"):
        if not self.is_moving:
            time.sleep(1)
            self.is_moving = True
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
        # if not self.is_moving:
        #     time.sleep(1)
        #     if last_point == "left":  # last point left goes right
        #         self.setheading(random.randint(-45, 0))
        #     else:  # last point right goes left
        #         self.setheading(random.randint(180, 225))
        #     self.is_moving = True
        # self.forward(BALL_SPEED)

    def bounce(self):
        """
        bounce behaviour when hitting the top or bottom of the screen
        """
        self.y_move *= -1
        # direction = self.heading()
        # #top of screen
        # if self.ycor() > 0:
        #     # ball going left
        #     if 90 < direction < 270:
        #         #bounce left
        #         self.setheading(direction + 90)
        #     # ball going right
        #     else:
        #         # bounce right
        #         self.setheading(direction - 90)
        # else:  # bottom of screen
        #     # going left
        #     if 90 < direction < 270:
        #         self.setheading(direction - 90)  # bounce right
        #     #going right
        #     else:
        #         self.setheading(direction + 90)  # bounce left

    def bounce_paddle(self):
        """
        bounce behaviour when hitting a paddle
        """
        self.x_move *= -1
        # direction = self.heading()
        # if paddle_side == "right":
        #     if 0 < direction < 90:  # ball is angled down, so turn right
        #         self.setheading(direction + 90)
        #     else:
        #         self.setheading(direction - 90)  # ball angled up, so turn left
        # else:
        #     if 0 < direction < 90:  # ball is angled down, so turn left
        #         self.setheading(direction - 90)
        #     else:
        #         self.setheading(direction + 90)  # ball angled up, so turn right

                # def start_moving(self):
    #     if not self.is_moving:
    #         self.setheading(0 + random.randint(-45,0))
    #         self.is_moving = True
