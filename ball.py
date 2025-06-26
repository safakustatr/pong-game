from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(30)
        self.step = 10

    def move(self):
        self.forward(self.step)

    def bounce(self):
        self.setheading(360 - self.heading())

    def bounce_from_paddle(self):
        self.setheading(180 - self.heading())

    def refresh(self):
        self.goto(0, 0)
        self.bounce_from_paddle()
        self.step = 10

    def speed_up(self):
        self.step += 5