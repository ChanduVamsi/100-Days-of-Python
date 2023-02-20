from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 28, "normal")

class Score(Turtle): 
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.goto(position)
        self.color("white")
        self.score = 0
        self.displayScore()
    
    def displayScore(self): 
        if self.score < 3: self.write(f"{self.score}", align=ALIGNMENT, font=FONT)
        else: self.write(f"WIN", align=ALIGNMENT, font=FONT)