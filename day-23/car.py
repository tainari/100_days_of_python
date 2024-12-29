import random, time
from turtle import Turtle

COLOURS = ["red", "orange", "yellow", "green", "blue", "purple"]
BASE_SPEED = 10

class Car(Turtle):
    def __init__(self, screen_width: int, screen_height: int, level: int = 1):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLOURS))
        self.penup()
        self.setheading(180)
        self.min_x = -screen_width // 2
        self.max_x = int(screen_width // 2 * 1.5)
        self.min_y = - screen_height // 2 + 50
        self.max_y = screen_height // 2 - 50
        self.increase_speed(level)
        self.initiate_position()

    def move(self):
        self.forward(self.speed)
        if self.xcor() < self.min_x - 50:
            self.reset_position()

    def initiate_position(self):
        self.hideturtle()
        new_x = random.randint(self.min_x, self.max_x)
        new_y = random.randint(-self.max_y, self.max_y)
        self.goto(x=new_x, y=new_y)
        self.showturtle()

    def reset_position(self):
        self.hideturtle()
        new_x = random.randint(self.max_x, int(self.max_x*1.2))
        new_y = random.randint(self.min_y, self.max_y)
        self.goto(x=new_x, y=new_y)
        self.showturtle()

    def increase_speed(self, level: int):
        self.speed = BASE_SPEED * (1 + 0.1 * (level - 1))