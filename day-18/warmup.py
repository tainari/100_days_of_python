from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")

def draw_shapes():
    for n_sides in range(3, 11):
        angle = 360 / n_sides
        for side in range(n_sides):
            timmy.forward(100)
            timmy.right(angle)

def random_walk(num_steps):
    for _ in range(num_steps):
        timmy.color((random.random(), random.random(), random.random()))
        timmy.forward(random.randint(1, 100))
        if random.random() < 0.5:
            timmy.right(random.randint(1, 360))
        else:
            timmy.left(random.randint(1, 360))

def spirograph(n_circles: int):
    turn_amount = 360 / n_circles
    timmy.speed(0)
    for _ in range(100):
        timmy.circle(100)
        timmy.right(turn_amount)

# random_walk(100)
spirograph(100)

screen = Screen()
screen.exitonclick()