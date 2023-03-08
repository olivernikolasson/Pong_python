import random
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_wid=0.80, stretch_len=0.80, outline=None)
        self.x_move = 0.08
        self.y_move = 0.08
        self.speed(10)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def out(self):
        self.goto(0,0)
        self.x_move *= -1

    def speedinc(self):
        self.x_move *= 1.05
        self.y_move *= 1.05
        print(self.x_move, self.y_move)

    def speedres(self):
        self.x_move = 0.08
        self.y_move = 0.08
        print(self.x_move, self.y_move)
