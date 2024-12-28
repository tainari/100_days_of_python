from turtle import Turtle

STEP_SIZE = 20
MARGIN = 30
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snek:
    def __init__(self):
        self.snek = []
        # Create initial snake with three body parts
        self.make_head()
        self.grow()
        self.grow()

    def make_head(self):
        box = Turtle(shape="square")
        box.color("white")
        box.penup()
        box.goto(0,0)
        self.snek.append(box)
        # Set head of snake
        self.head = self.snek[0]


    def grow(self):
        box = Turtle(shape="square")
        box.color("white")
        box.penup()
        last_box = self.snek[-1]
        if last_box.heading() == RIGHT:
            box.goto(x=last_box.xcor()-STEP_SIZE, y=last_box.ycor())
        elif last_box.heading() == LEFT:
            box.goto(x=last_box.xcor()+STEP_SIZE, y=last_box.ycor())
        elif last_box.heading() == UP:
            box.goto(x=last_box.xcor(), y=last_box.ycor()-STEP_SIZE)
        elif last_box.heading() == DOWN:
            box.goto(x=last_box.xcor(), y=last_box.ycor()+STEP_SIZE)
        else:
            print("Danger, Will Robinson.")
        self.snek.append(box)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move(self):
        n_boxes = len(self.snek)
        for ind in range(n_boxes-1, 0, -1):
            box = self.snek[ind]
            prev_box = self.snek[ind-1]
            box.goto(prev_box.xcor(), prev_box.ycor())
        self.head.forward(STEP_SIZE)

    def has_wall_collision(self, screen_size):
        hit_left_wall = self.head.xcor() < -screen_size // 2 + MARGIN
        hit_right_wall = self.head.xcor() > screen_size // 2 - MARGIN
        hit_top_wall = self.head.ycor() < -screen_size // 2 + MARGIN
        hit_bottom_wall = self.head.ycor() > screen_size // 2 - MARGIN
        return hit_left_wall or hit_right_wall or hit_top_wall or hit_bottom_wall

    def has_self_collision(self):
        for box in self.snek[2:]:
            if self.head.distance(box) < 10:
                return True