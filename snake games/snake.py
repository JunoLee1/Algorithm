from turtle import Turtle
STARTINING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake(Turtle):
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTINING_POSITION:
            self.add_segment(position)
    
    def add_segment(self,position):
        new_position = Turtle("square")
        new_position.color("white")
        new_position.penup()
        new_position.goto(position)
        self.segments.append(new_position) 

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
           new_x = self.segments[i-1].xcor()
           new_y = self.segments[i-1].ycor()
           self.segments[i].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)