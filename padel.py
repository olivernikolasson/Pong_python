from turtle import Turtle
UPH = 90
DPH = 270
FOW = 35

class Padel(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.penup()
        self.turtlesize(stretch_wid=0.20, stretch_len=5, outline=None)
        self.goto(position)

    def up(self):
        self.setheading(UPH)
        self.forward(FOW)

    def down(self):
        self.setheading(DPH)
        self.forward(FOW)


