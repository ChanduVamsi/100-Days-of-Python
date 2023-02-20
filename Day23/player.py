from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black", "Beige")
        self.shape("turtle")
        self.setheading(90)
        self.speed(0)
        self.shapesize(stretch_len=1.5, stretch_wid=1.5)
        self.goto(0, -250)