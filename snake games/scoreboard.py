from turtle import Turtle
file = open("new.txt", mode = "w") 
FONT = ("Ariel", 24, "normal")
ALIGN = "center"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            
        self.score = 0
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"score: {self.score} high score: {self.high_score}",align=ALIGN, font = FONT)

    def increase(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

   
    


