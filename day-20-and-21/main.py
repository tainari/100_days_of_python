"""
it's snake!
"""
import time
from turtle import Turtle, Screen
from snek import Snek

SCREEN_SIZE = 800

screen = Screen()
screen.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
screen.bgcolor("black")
screen.title("Snek!")
screen.tracer(0)

snake = Snek()

screen.listen()
screen.onkey(fun=snake.left, key="a")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="d")
screen.onkey(fun=snake.right, key="Right")

for _ in range(100):
    snake.move()
    screen.update()
    time.sleep(0.5)

screen.exitonclick()
