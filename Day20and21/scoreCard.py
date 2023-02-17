from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")

high_score = 0

class ScoreCard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(200, 300)
    
    def displayScore(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score: {high_score}", align=ALIGNMENT, font=FONT)
    
    def addScore(self):
        global high_score
        self.score += 1
        if self.score > high_score: high_score = self.score
    
    def gameOver(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Courier", 48, "normal"))
