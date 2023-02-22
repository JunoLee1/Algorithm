from turtle import Turtle
FONT = ("Courier", 80, "normal")
ALIGN = "center"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(-100, 200)
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.write(self.l_score, align = ALIGN, font = FONT)
        self.goto(100, 200)
        self.hideturtle()
        self.write(self.r_score, align = ALIGN, font = FONT)
    
    