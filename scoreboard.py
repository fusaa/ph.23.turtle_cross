from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280,280)
        self.score = 0
        self.write(f"Score: {self.score}")

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}")

    def game_over(self):
        self.goto(-50,0)
        self.write("Game Over")



