import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carmanger = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanger.create_car()
    carmanger.move_cars()
    
    for car in carmanger.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() > 280:
        scoreboard.current_level()
        player.go_to_starting_pos()
        carmanger.speed_up()

screen.exitonclick()
