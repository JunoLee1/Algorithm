from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("White")
        self.penup()
        self.dx = 10
        self.dy = 10
        self.speed = 0.1
    
    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x,new_y)


    def bounce(self):
        self.dy *= -1 # to reflect the ball

    def reflect(self):
        self.dx *= -1
        self.speed *= 0.9


    def reset(self):
        self.goto(0, 0)
        self.speed = 0.1
        self.reflect()