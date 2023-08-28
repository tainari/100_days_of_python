from turtle import Turtle

class Frog(Turtle):
    MOVE_SPEED = 10
    def __init__(self, window_size: int):
        super().__init__()
        self.window_size = window_size
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.up()
        self.reset_position()


    def move(self):
        self.forward(self.MOVE_SPEED)

    def reset_position(self):
        self.sety(-self.window_size//2 + 20)