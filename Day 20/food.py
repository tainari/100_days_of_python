from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("white")
        self.speed("fastest")
        self.move()
    def move(self):
        rand_x = random.randint(-14,14) * 20
        rand_y = random.randint(-14,14) * 20
        self.goto(rand_x,rand_y)
