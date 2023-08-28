import turtle
from turtle import Turtle

PADDLE_HEIGHT = 6
TURTLE_SIZE = 20
STEP_SIZE = 15

class Paddle(Turtle):
    def __init__(self,window_width=1000, window_height=500, side="left"):
        super().__init__()
        self.max_y = window_height // 2
        self.min_y = -window_height // 2
        if side == "left":
            self.create_paddle(side,-window_width//2 + TURTLE_SIZE//2)
        else:
            self.create_paddle(side,window_width//2 - TURTLE_SIZE)
        # self.top = self.paddle[0]
        # self.bottom = self.paddle[-1]


    def create_paddle(self,side, x_pos):
        self.shape("square")
        self.turtlesize(stretch_wid=5,stretch_len=1)
        self.color("white")
        self.up()
        self.setpos(x_pos,0)
        # return paddle
        # paddle = []
        # y_pos = PADDLE_HEIGHT * TURTLE_SIZE / 2
        # for i in range(PADDLE_HEIGHT):
        #     t = Turtle()
        #     t.shape("square")
        #     t.color("white")
        #     t.up()
        #     t.setposition(x_pos,y_pos)
        #     paddle.append(t)
        #     y_pos -= TURTLE_SIZE



    def move_up(self):
        top = self.ycor() + 50
        if top < self.max_y:
            self.sety(self.ycor() + STEP_SIZE)
            # print("up up up")
            # for t in self.paddle:
            #     # print(t.ycor())
            #     t.sety(t.ycor() + 10)
        else:
            pass

    def move_down(self):
        bottom = self.ycor() - 50
        if bottom > self.min_y + 10:
            self.sety(self.ycor() - STEP_SIZE)
            # print("down to the  yoululierah")
            # for t in self.paddle:
            #     t.sety(t.ycor() - 10)
            # for ind in range(PADDLE_HEIGHT-1,1,-1):
            #     new_x = self.paddle[ind-1].xcor()
            #     new_y = self.paddle[ind-1].ycor()
            #     self.paddle[ind].setposition(new_x,new_y)
