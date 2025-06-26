from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setup(side)

    def setup(self, side):
        if side == "left":
            self.goto(-350, 0)
        else:
            self.goto(350, 0)

    def go_up(self):
        self.forward(20)

    def go_down(self):
        self.backward(20)
