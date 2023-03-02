FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(x = -250, y = 270)
        self.write(f"level: {self.level}", align = "Center", font = FONT)


    def current_level(self):
        self.level += 1
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"score{self.level}", align = "Center", font = FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align = "Center", font = FONT)