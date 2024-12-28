from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, side: str, canvas_width: int, canvas_height: int):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        # move to side of screen
        if side == "left":
            self.goto(-canvas_width/2 + 20, 0)
        elif side == "right":
            self.goto(canvas_width/2 - 20, 0)
        else:
            print("Invalid side")
        self.showturtle()
        self.max_y = canvas_height / 2 - 50

    def up(self):
        if self.ycor() < self.max_y:
            self.goto(self.xcor(), self.ycor()+20)

    def down(self):
        if self.ycor() > -self.max_y:
            self.goto(self.xcor(), self.ycor()-20)

    def all_done(self):
        self.clear()
        self.hideturtle()