from turtle import Screen
from car_manager import CarManager
from frog import Frog
from scoreboard import Scoreboard

WINDOW_SIZE = 600

screen = Screen()
screen.setup(width=WINDOW_SIZE,height=WINDOW_SIZE)
screen.title('Turtler')
screen.tracer(0)

cars = CarManager(WINDOW_SIZE)
frog = Frog(WINDOW_SIZE)
scoreboard = Scoreboard(WINDOW_SIZE)

screen.listen()
screen.onkey(frog.move,'w')
screen.onkey(frog.move,'Up')

playing = True

while playing:
    playing = cars.move_cars(frog)
    if frog.ycor() >= WINDOW_SIZE // 2 - 10:
        scoreboard.increase_score()
        frog.reset_position()
        cars.reset_car_positions()
    screen.update()

scoreboard.game_over()

screen.exitonclick()