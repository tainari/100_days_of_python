from turtle import Turtle

TEXT_ALIGNMENT = "center"
TEXT_FONT = "Courier"
TEXT_FONT_SIZE = 20
BIG_FONT_SIZE = 40
TEXT_STYLE = "normal"
class Score(Turtle):
    def __init__(self,window_dimension = 600):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.setposition(x=0,y=window_dimension//2 - 30)
        self.score = 0
        self.max_score = self.get_max_score()
        self.score_increment = 1
        self.print_score()

    def get_max_score(self):
        max_score = None
        try:
            with open('snek_high_score.txt','r') as f:
                max_score = int(f.readline())
        except (TypeError,FileNotFoundError):
            max_score = 0
        return max_score

    def print_score(self):
        self.write(f"Score: {self.score}\tMax Score: {self.max_score}",align=TEXT_ALIGNMENT, font=(TEXT_FONT, TEXT_FONT_SIZE, TEXT_STYLE))
    def increase_score(self):
        self.score += self.score_increment
        self.clear()
        self.print_score()

    def user_loses(self):
        # self.setposition(x=0,y=0)
        # self.write("YOU LOSE 💀",align=TEXT_ALIGNMENT, font=(TEXT_FONT, BIG_FONT_SIZE, TEXT_STYLE))
        if self.score > self.max_score:
            self.max_score = self.score
            with open('snek_high_score.txt','w') as f:
                f.write(str(self.score))