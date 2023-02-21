from turtle import Screen
from snake import Snake
from food import Food
from scoreCard import ScoreCard

gameOn = True

def canvasSetup():
    global canvas
    canvas.screensize(600, 600)
    canvas.bgcolor("black")
    canvas.title("My Snake Game")
    canvas.tracer(0)

def gameControls():
    global canvas, silly
    canvas.listen()
    canvas.onkey(fun=silly.up, key='Up')
    canvas.onkey(fun=silly.down, key='Down')
    canvas.onkey(fun=silly.left, key='Left')
    canvas.onkey(fun=silly.right, key='Right')

canvas = Screen()
canvasSetup()
silly = Snake()
snack = Food()
banner = ScoreCard()
gameControls()
score = 0

while gameOn: 
    banner.displayScore()
    silly.move()
    canvas.update()

    # If the snake eats the food
    if silly.head.distance(snack) < 15:
        silly.extend()
        snack.refresh()
        banner.score += 1
    
    # If the snake collides with the walls
    if (silly.head.xcor() > 320 or silly.head.xcor() < -350 or silly.head.ycor() > 320 or silly.head.ycor() < -300): 
        banner.score = 0
        silly.resetSnake()
    
    # If the snake collides with it's tail
    for part in silly.snake[:0:-1]: 
        if silly.head.distance(part) < 10: 
            banner.score = 0
            silly.resetSnake()
            break

# banner.gameOver()
canvas.exitonclick()