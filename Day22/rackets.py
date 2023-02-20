from turtle import Turtle

class Racket(Turtle):
    def __init__(self, position):
        super().__init__()
        self.speed(0)
        self.penup()
        self.setheading(90)
        self.color("white")
        self.goto(position)
        self.shape("square")
        self.shapesize(stretch_len=5, stretch_wid=1)

    def up(self):
        y = self.ycor()
        if y < 280: self.goto(self.xcor(), y + 40)
    
    def down(self):
        y = self.ycor()
        if y > -280: self.goto(self.xcor(), y - 40)

