from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.max_score = 50
        # get ready to write
        self.penup()
        self.color("black")
        self.hideturtle()

    def update_level(self):
        self.clear()
        self.goto(x=0, y=self.y)
        self.write(self.level, move=False, align="center", font=("Courier", 15, "normal"))

    def add_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER :(", move=False, align="center", font=("Courier", 20, "normal"))