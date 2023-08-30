from turtle import Turtle

MOVE_DISTANCE = 20
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180
class Snake():
    def __init__(self,window_dimension = 600):
        # colours = ['red', 'yellow', 'orange', 'green', 'blue', 'purple']
        self.body = []
        self.start_len = 3
        self.len = 0
        self.occupied_spaces = set()
        self.create_snake()
        self.head = self.body[0]
        self.max_coord = window_dimension / 2 - 10
        self.min_coord = -window_dimension / 2 + 10

    def reset_snek(self):
        for seg in self.body:
            seg.goto(x=1000,y=1000)
        self.body = []
        self.occupied_spaces = set()
        self.len = 0
        self.create_snake()
        self.head = self.body[0]
    def create_snake(self):
        x_coord = 0
        for i in range(self.start_len):
            self.add_segment(x_coord,0)
            x_coord -= 20
        print(self.body)

    def add_segment(self,x,y):
        t = Turtle(shape='square')
        t.up()
        t.color("white")
        t.setx(x)
        t.sety(y)
        self.body.append(t)
        self.occupied_spaces.add((x,y))
        self.len += 1

    def increase_body(self):
        tail = self.body[-1]
        tail_x = 10 * round(int(tail.xcor()) / 10)
        tail_y = 10 * round(int(tail.ycor()) / 10)
        tail_orientation = tail.heading()
        if tail_orientation == NORTH:
            self.add_segment(tail_x,tail_y-20)
        elif tail_orientation == SOUTH:
            self.add_segment(tail_x,tail_y+20)
        elif tail_orientation == EAST:
            self.add_segment(tail_x-20,tail_y)
        else:
            self.add_segment(tail_x+20,tail_y)
    def up(self):
        if self.head.heading() != SOUTH:
            self.head.setheading(NORTH)

    def right(self):
        if self.head.heading() != WEST:
            self.head.setheading(EAST)

    def down(self):
        if self.head.heading() != NORTH:
            self.head.setheading(SOUTH)

    def left(self):
        if self.head.heading() != EAST:
            self.head.setheading(WEST)

    def check_collision(self):
        head_x = int(self.head.xcor())
        head_y = int(self.head.ycor())
        if (head_x,head_y) in self.occupied_spaces:
            print("Hit!")
            return False
        elif head_x > self.max_coord or head_x < self.min_coord or head_y > self.max_coord or head_y < self.min_coord:
            print("Wall!")
            return False
        else:
            self.occupied_spaces.add((head_x,head_y))
            return True

    def got_food(self,pos):
        food_x, food_y = pos
        return (self.head.xcor() - 10 <= food_x <= self.head.xcor() + 10) and (self.head.ycor() - 10 <= food_y <= self.head.ycor() + 10)

    def move(self):
        # tail = self.body[-1]
        # tail_x = 10 * round(int(tail.xcor()) / 10)
        # tail_y = 10 * round(int(tail.ycor()) / 10)
        self.occupied_spaces = set()
        for segment_index in range(self.len - 1, 0, -1):
            new_x = int(self.body[segment_index - 1].xcor())
            new_y = int(self.body[segment_index - 1].ycor())
            self.body[segment_index].setposition(new_x, new_y)
            self.occupied_spaces.add((new_x,new_y))
        # print(self.occupied_spaces)
        # self.occupied_spaces.remove((tail_x, tail_y))
        self.head.forward(MOVE_DISTANCE)
        return self.check_collision()