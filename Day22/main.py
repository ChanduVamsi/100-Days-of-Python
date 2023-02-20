from turtle import Turtle, Screen
from rackets import Racket
from ball import Ball
from scores import Score
from time import sleep

def canvasSetup():
    global canvas
    canvas.screensize(710,600)
    canvas.bgcolor("black")
    canvas.tracer(0)

def divider():
    divider_object = Turtle()
    divider_object.color("white")
    divider_object.speed(0)
    divider_object.pensize(3)
    divider_object.hideturtle()
    divider_object.penup()
    divider_object.setheading(270)
    for ycor in range(340, -340, -20):
        divider_object.goto(0, ycor)
        if ycor % 40 != 0: divider_object.pendown()
        else: divider_object.penup()
        divider_object.forward(20)

def setGameControls(player, up, down):
    global canvas
    canvas.listen()
    canvas.onkey(fun=player.up, key=up)
    canvas.onkey(fun=player.down, key=down)

canvas = Screen()
canvasSetup()

divider()

player1 = Racket((-330, 0))
score1 = Score((-180, 290))
setGameControls(player1, "w", "s")

player2 = Racket((330, 0))
score2 = Score((180, 290))
setGameControls(player2, "Up", "Down")

ping_pong = Ball()

while score1.score < 3 and score2.score < 3: 
    sleep(ping_pong.move_speed)
    canvas.update()
    ping_pong.move()
    # Detect collision with wall
    if ping_pong.ycor() > 300 or ping_pong.ycor() < -300: ping_pong.bounce()
    # Detect hit with the racket
    if (ping_pong.distance(player1) < 50 and ping_pong.xcor() < -300) or (ping_pong.distance(player2) < 50 and ping_pong.xcor() > 300): ping_pong.hit()
    # Detect ball missed
    if ping_pong.xcor() > 380: 
        score1.clear()
        score1.score += 1
        ping_pong.miss()
    elif ping_pong.xcor() < -380: 
        score2.clear()
        score2.score += 1
        ping_pong.miss()
    score1.displayScore()
    score2.displayScore()

canvas.exitonclick()