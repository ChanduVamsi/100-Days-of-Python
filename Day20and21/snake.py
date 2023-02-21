from turtle import Turtle
from time import sleep

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake = []
        self.snakeSetup()
        self.head = self.snake[0]

    def snakeSetup(self):
        for position in STARTING_POSITIONS:
            self.addPart(position)
    
    def move(self):
        sleep(0.036)
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].goto(self.snake[i-1].position())
        self.head.forward(MOVE_DISTANCE)
    
    def addPart(self, position):
        snake_part = Turtle("square")
        snake_part.color("Chartreuse")
        snake_part.penup()
        snake_part.speed(1)
        snake_part.goto(position)
        self.snake.append(snake_part)

    def extend(self):
        position = self.snake[-1].position()
        self.addPart(position)
    
    def resetSnake(self):
        for part in self.snake: part.goto(1000,1000)
        self.snake.clear()
        self.snake = []
        self.snakeSetup()
        self.head = self.snake[0]
        sleep(2)

    def up(self): 
        if self.head.heading() != DOWN: self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP: self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT: self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT: self.head.setheading(RIGHT)
