import random, time
from turtle import Turtle

MOVEMENT_SPEED = 20

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        # pick random direction to start
        self.setheading(random.randint(0,360))
        # set movement speed
        if 90 < self.heading() < 270:
            self.x_move = -MOVEMENT_SPEED
            self.y_move = -MOVEMENT_SPEED
        else:
            self.x_move = MOVEMENT_SPEED
            self.y_move = MOVEMENT_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_paddle(self):
        self.x_move *= -1

    def bounce_wall(self):
        self.y_move *= -1

    def reset_ball(self, scoring_player: int):
        self.hideturtle()
        self.goto(0, 0)
        for ct in range(3,0,-1):
            self.write(ct, align="center", font=("Arial", 24, "bold"))
            time.sleep(1)
            self.clear()
        self.showturtle()
        # set direction of ball towards player who scored most recently
        if scoring_player == 1:
            self.setheading(random.randint(90,270))
            self.x_move = -MOVEMENT_SPEED
            self.y_move = -MOVEMENT_SPEED
        else:
            self.setheading(random.choice([random.randint(0,90),random.randint(270,360)]))
            self.x_move = MOVEMENT_SPEED
            self.y_move = MOVEMENT_SPEED

    def all_done(self):
        self.clear()
        self.hideturtle()