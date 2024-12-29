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

cars = []
for _ in range(20):
    car = Car(screen_height=SCREEN_HEIGHT, screen_width=SCREEN_WIDTH, level = current_level.level)
    cars.append(car)
frogger = Frog(screen_height=SCREEN_HEIGHT)

screen.listen()
screen.onkey(frogger.up, "Up")
screen.onkey(frogger.down, "Down")

game_over = False
while not game_over:
    while frogger.ycor() < frogger.end_y:
        screen.update()
        time.sleep(0.1)
        for car in cars:
            car.move()
            if car.distance(frogger) < 20:
                game_over = True
                break


current_level.game_over()

screen.exitonclick()