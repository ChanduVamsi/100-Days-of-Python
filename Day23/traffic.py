import random
from turtle import Turtle

COLOURS = ["Brown", "white", "DarkGreen", "RoyalBlue"]
LANES = [185, 115, 45, -35, -105, -175]
SPEEDS = [1,2,3,4,5,6,7,8]

cars = []

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1.1)
        self.color("black", random.choice(COLOURS))
        self.ycor = random.choice(LANES)
        self.xcor = 340
        self.penup()
        self.setheading(180)
        self.goto(self.xcor, self.ycor)
    
    def resetCarPosition(self):
        self.ycor = random.choice(LANES)
        self.goto(340, self.ycor)
