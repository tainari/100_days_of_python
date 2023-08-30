from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score


screen = Screen()
WINDOW_DIMENSION = 600
screen.setup(width=WINDOW_DIMENSION,height=WINDOW_DIMENSION)
screen.bgcolor('black')
screen.title("Snek")

screen.tracer(0)
snek = Snake(WINDOW_DIMENSION)
current_score = Score()

screen.update()

screen.listen()
screen.onkey(snek.right,'d')
screen.onkey(snek.down,'s')
screen.onkey(snek.left,'a')
screen.onkey(snek.up,'w')
screen.onkey(snek.right,'Right')
screen.onkey(snek.down,'Down')
screen.onkey(snek.left,'Left')
screen.onkey(snek.up,'Up')

nom = Food()

def play_game():
    game_active = True
    while game_active:
        screen.update()
        time.sleep(.1)
        point = snek.got_food(tuple(nom.pos()))
        if point:
            current_score.increase_score()
            snek.increase_body()
            nom.move()
        game_active = snek.move()
        if not game_active:
            current_score.user_loses()
            snek.reset_snek()
            screen.update()
            nom.move()
            game_active = True

screen.onkey(play_game,' ')

play_game()

screen.exitonclick()