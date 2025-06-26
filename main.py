# TODO 1: Create the screen                     # Done
# TODO 2: Create and move the paddle            # Done
# TODO 3: Create another paddle                 # Done
# TODO 4: Create the ball and make it move
# TODO 5: Detect collision with ball and bounce
# TODO 6: Detect collision with paddle
# TODO 7: Detect when paddle misses
# TODO 8: Keep score

from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

p1_paddle = Paddle("right")
p2_paddle = Paddle("left")

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(p1_paddle.go_up, "Up")
screen.onkey(p1_paddle.go_down, "Down")
screen.onkey(p2_paddle.go_up, "w")
screen.onkey(p2_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    p1_condition_hit = ball.distance(p1_paddle) < 50 and ball.xcor() > 320
    p2_condition_hit = ball.distance(p2_paddle) < 50 and ball.xcor() < -320
    p1_condition_miss = ball.xcor() > 380
    p2_condition_miss = ball.xcor() < -380

    if p1_condition_hit or p2_condition_hit:
        ball.bounce_from_paddle()
        ball.speed_up()

    if p1_condition_miss:
        ball.refresh()
        scoreboard.p2_score += 1
        scoreboard.refresh()
    if p2_condition_miss:
        ball.refresh()
        scoreboard.p1_score += 1
        scoreboard.refresh()

screen.exitonclick()