"""
it's snake!
"""
import time
from turtle import Turtle, Screen
from snek import Snek
from food import Food
from score import Score

SCREEN_SIZE = 800

screen = Screen()
screen.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
screen.bgcolor("black")
screen.title("Snek!")
screen.tracer(0)

snake = Snek()
food = Food(screen_size=SCREEN_SIZE)
scoreboard = Score(screen_size=SCREEN_SIZE)

# control snake with WASD or arrow keys
screen.listen()
screen.onkey(fun=snake.left, key="a")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="d")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.up, key="w")
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="s")
screen.onkey(fun=snake.down, key="Down")

game_on = True
while game_on:
    snake.move()
    screen.update()
    time.sleep(0.1)
    if snake.head.distance(food) < 20:
        food.move_food()
        scoreboard.add_point()
        snake.grow()
    # check for collisions
    if snake.has_wall_collision(screen_size=SCREEN_SIZE) or snake.has_self_collision():
        game_on = False
        scoreboard.game_over()

screen.exitonclick()
