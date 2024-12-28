from turtle import Turtle

class Score(Turtle):
    def __init__(self, screen_height: int):
        super().__init__()
        self.player_1 = 0
        self.player_2 = 0
        # get ready to write
        self.penup()
        self.color("white")
        self.hideturtle()
        self.y = screen_height / 2 * 0.9
        # write score
        self.update_score()

    def update_score(self):
        score = f"Player 1: {self.player_1} | Player 2: {self.player_2}"
        self.clear()
        self.goto(x=0, y=self.y)
        self.write(score, move=False, align="center", font=("Courier", 15, "normal"))

    def add_point(self, player: int):
        if player == 1:
            self.player_1 += 1
        elif player == 2:
            self.player_2 += 1
        else:
            print("Invalid player")
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        final_score = f"Player {1 if self.player_1 > self.player_2 else 2} wins!"
        self.write(final_score, move=False, align="center", font=("Courier", 20, "normal"))