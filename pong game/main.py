from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong game")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed())
    screen.update()
    ball.move()
    #detect colision with wall
    if ball.ycor() > 280 or ball.ycor() < -280: 
        ball.bounce()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330:
        ball.reflect()
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.reflect()
    # detect right side bar miss the ball
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_score += 1


    elif ball.xcor() < -380:
        ball.reset()
        scoreboard.r_score += 1

   


screen.exitonclick() 