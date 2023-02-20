from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 28, "normal")

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.score = 0
        self.hideturtle()
        self.color("white")
    
    def display(self, gameisOn=True):
        self.clear()
        self.penup()
        self.goto(0, 280)
        if not gameisOn: self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
        elif self.level == 6: self.write("YOU WON!", align=ALIGNMENT, font=FONT)
        else: self.write(f"LEVEL {self.level}", align=ALIGNMENT, font=FONT) 
        self.goto(310,310)
        self.write(f"score: {self.score}", align=ALIGNMENT, font=16) 
        self.goto(270 ,340)
        self.pendown()
        self.pensize(2)
        self.setheading(270)
        self.forward(44)
        self.setheading(0)
        self.forward(80)

    def nextLevel(self):
        self.level += 1
        self.score += self.level
        self.display()
