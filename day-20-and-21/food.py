from turtle import Turtle
import random

MARGIN = 30

class Food(Turtle):
    def __init__(self, screen_size):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.speed("fastest")
        self.x_min = -screen_size // 2 + MARGIN
        self.x_max = screen_size // 2 - MARGIN
        self.y_min = -screen_size // 2 + MARGIN
        self.y_max = screen_size // 2 - MARGIN
        self.move_food()

    def move_food(self):
        self.goto(random.randint(self.x_min, self.x_max), random.randint(self.y_min, self.y_max))