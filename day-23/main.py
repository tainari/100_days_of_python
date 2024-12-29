import time

from car import Car
from frog import Frog
from level import Level
from turtle import Screen

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("white")
screen.title("Frogger (but not)")
screen.tracer(0)

current_level = Level(screen_height=SCREEN_HEIGHT)

def initiate_cars(screen_height, screen_width, level, num_cars = 20):
    cars = []
    for _ in range(num_cars):
        car = Car(screen_height=screen_height, screen_width=screen_width, level = level)
        cars.append(car)
    return cars

def reset_cars(cars, level):
    for car in cars:
        car.increase_speed(level)
        car.initiate_position()


frogger = Frog(screen_height=SCREEN_HEIGHT)

screen.listen()
screen.onkey(frogger.up, "Up")
screen.onkey(frogger.down, "Down")

not_dead_yet = True
game_over = False
cars = initiate_cars(screen_height=SCREEN_HEIGHT, screen_width=SCREEN_WIDTH, level=current_level.level)

while not game_over:
    screen.update()
    time.sleep(0.1)
    for car in cars:
        if car.distance(frogger) < 20:
            game_over = True
            break
        car.move()

    if frogger.ycor() >= frogger.end_y:
        frogger.reset_position()
        current_level.add_level()
        reset_cars(cars, current_level.level)

current_level.game_over()

screen.exitonclick()