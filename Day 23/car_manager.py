import random
from turtle import Turtle
from turtle_colours import colours

NUM_CARS_TO_CREATE = 50
SPEED_CHANGE = 1.25
class CarManager():
    def __init__(self,window_size):
        self.cars = [Car(window_size) for _ in range(NUM_CARS_TO_CREATE)]

    def move_cars(self, frog):
        for c in self.cars:
            collision = c.drive_forward(frog)
            if collision:
                return False
            if c.xcor() < -c.window_max-20:
                c.set_random_position(1)
        return True


    def reset_car_positions(self):
        for c in self.cars:
            c.set_random_position(SPEED_CHANGE)


class Car(Turtle):
    def __init__(self,window_size: int):
        super().__init__()
        self.up()
        self.shape("square")
        self.turtlesize(stretch_wid=1,stretch_len=2)
        self.color(random.choice(colours))
        self.setheading(180)
        self.window_max = window_size // 2
        self.move_speed = 0.5
        self.set_random_position(1)

    def set_random_position(self,speed_change):
        self.setx(random.randint(self.window_max-100,5 * self.window_max))
        self.sety(random.randint(-self.window_max+40,self.window_max-40))
        self.move_speed *= speed_change

    def drive_forward(self, frog):
        self.forward(self.move_speed)
        collision = (abs(frog.ycor() - self.ycor()) < 10
                     and
                     self.distance(frog) < 20)
        return collision