from turtle import Turtle
TEXT_ALIGNMENT = "center"
TEXT_FONT = "Courier"
TEXT_FONT_SIZE = 20
BIG_FONT_SIZE = 40
TEXT_STYLE = "normal"
class Scoreboard(Turtle):
    def __init__(self,window_height = 500):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.setposition(x=0,y=window_height//2 - 30)
        self.left_score = 0
        self.right_score = 0
        self.max_points = 0
        self.score_increment = 1
        self.print_score()

    def print_score(self):
        self.write(f"{self.left_score}\t\t\t\t{self.right_score}",align=TEXT_ALIGNMENT, font=(TEXT_FONT, TEXT_FONT_SIZE, TEXT_STYLE))
    def increase_score(self,side):
        if side == "left":
            self.left_score += 1
        else:
            self.right_score += 1
        self.max_points = max(self.left_score,self.right_score)
        self.clear()
        self.print_score()

    def game_over(self,winner):
        self.setposition(x=0,y=0)
        self.write(f"{winner} wins!",align=TEXT_ALIGNMENT, font=(TEXT_FONT, BIG_FONT_SIZE, TEXT_STYLE))