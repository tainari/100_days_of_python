from turtle import Turtle

class Frog(Turtle):
    def __init__(self, screen_height: int):
        super().__init__()
        self.hideturtle()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.showturtle()
        self.start_y = -screen_height//2 + 20
        self.end_y = screen_height//2 - 20
        self.reset_position()


    def up(self):
        self.forward(20)

    def down(self):
        self.forward(-20)

    def reset_position(self):
        self.hideturtle()
        self.goto(0, self.start_y)
        self.showturtle()