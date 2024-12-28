from turtle import Turtle
import csv

class Score(Turtle):
    def __init__(self, screen_size):
        super().__init__()
        # initiate score numbers
        self.score = 0
        self.get_high_score()
        # get ready to write
        self.penup()
        self.color("white")
        self.hideturtle()
        self.screen_size = screen_size
        # write score
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(x=0, y=self.screen_size / 2 - 50)
        self.write(f"Score: {self.score}", move=False, align="center",font=("Courier", 20, "normal"))
        self.goto(x=0, y=self.screen_size / 2 - 70)
        self.write(f"High Score: {self.high_score}", move=False, align="center",font=("Courier", 15, "bold"))

    def add_point(self):
        self.score += 1
        self.update_score()

    def save_high_score(self):
        pass

    def game_over(self):
        self.high_score = max(self.high_score, self.score)
        # print(f"High Score: {self.high_score}")
        with open("high_score.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow([self.high_score])
        self.score = 0

    def get_high_score(self):
        self.high_score = 0
        with open("high_score.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                self.high_score = int(row[0])
        # print(f"Loaded High Score: {self.high_score}")