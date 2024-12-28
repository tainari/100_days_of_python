from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, side: str, canvas_width: int):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=0.5, stretch_len=3)
        self.setheading(90)
        # move to side of screen
        if side == "left":
            self.goto(-canvas_width/2 + 20, 0)
        elif side == "right":
            self.goto(canvas_width/2 - 20, 0)
        else:
            print("Invalid side")
        self.showturtle()

    def up(self):
        self.forward(20)

    def down(self):
        self.forward(-20)