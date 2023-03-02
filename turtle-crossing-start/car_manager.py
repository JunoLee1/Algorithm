COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random



class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []   #cant' understand
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)  #probability 1 out of 6
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.turtlesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)  # can't understand

    def move_cars(self):
       for car in self.all_cars:
           car.backward(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
    
