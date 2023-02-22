from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.tracer(0)
#to organise the segments 
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen() # to use onkey function, listen function is far important to use
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


the_game_on = True
while the_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase()

    elif snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280: 
        the_game_on = False
# detect collison with tail.
# we had colide any seg, trig game over sig
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            the_game_on = False


screen.exitonclick()
    

