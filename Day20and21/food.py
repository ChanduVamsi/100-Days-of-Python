import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("GhostWhite")
        self.speed(0)
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.refresh()
    
    def refresh(self):
        xcor = random.randint(-300, 300)
        ycor = random.randint(-300, 300)
        self.goto(xcor, ycor)