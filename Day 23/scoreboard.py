from turtle import Turtle
TEXT_ALIGNMENT = "left"
GAME_OVER_TEXT_ALIGNMENT = "center"
TEXT_FONT = "Courier"
TEXT_FONT_SIZE = 20
BIG_FONT_SIZE = 40
TEXT_STYLE = "normal"
class Scoreboard(Turtle):
    def __init__(self,window_size = 500):
        super().__init__()
        self.hideturtle()
        self.pencolor("black")
        self.penup()
        self.setposition(x=-window_size//2 + 30,y=window_size//2 - 30)
        self.level = 1
        self.print_score()

    def print_score(self):
        self.write(f"Level {self.level}",align=TEXT_ALIGNMENT, font=(TEXT_FONT, TEXT_FONT_SIZE, TEXT_STYLE))
    def increase_score(self):
        self.level += 1
        self.clear()
        self.print_score()

    def game_over(self):
        self.setposition(x=0,y=0)
        self.write(f"You lose. 💀",align=GAME_OVER_TEXT_ALIGNMENT, font=(TEXT_FONT, BIG_FONT_SIZE, TEXT_STYLE))