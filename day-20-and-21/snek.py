from turtle import Turtle, Screen
STEP_SIZE = 20

class Snek:
    def __init__(self):
        self.snek = []
        y = 0
        x = 0
        colors=['white','red','blue']
        for i in range(3):
            box = Turtle(shape="square")
            # box.color(colors[i])
            box.color("white")
            box.penup()
            box.goto(x, y)
            x -= STEP_SIZE
            self.snek.append(box)

    def left(self):
        self.snek[0].left(90)

    def right(self):
        self.snek[0].right(90)

    def move(self, turn:int = 0):
        n_boxes = len(self.snek)
        for ind in range(n_boxes-1, 0, -1):
            box = self.snek[ind]
            prev_box = self.snek[ind-1]
            box.goto(prev_box.xcor(), prev_box.ycor())
        # self.snek[0].left(turn)
        self.snek[0].forward(STEP_SIZE)