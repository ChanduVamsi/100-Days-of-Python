from turtle import Turtle
from time import sleep

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 8
        self.y_move = 10
        self.move_speed = 0.03

    def move(self):
        xcor, ycor = self.xcor(), self.ycor()
        self.goto(xcor + self.x_move, ycor + self.y_move)
    
    def bounce(self): self.y_move *= -1
    def hit(self): 
        self.x_move *= -1
        self.move_speed -= 0.002

    def miss(self):
        self.move_speed = 0.03
        self.goto(0,0)
        sleep(0.95)
        self.x_move *= -1
