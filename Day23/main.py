import random

from turtle import Turtle, Screen
from player import Player
from traffic import Car
from level import Level
from time import sleep

ROAD_BORDER = 5
LANE_LINE = 4
DIVIDER = 1
speeds = [3,4,5,6,7,8,9,0]

def drawRoad(position, line_width, lane):
    global paint
    paint.pensize(line_width)
    paint.penup()
    paint.goto(position)
    paint.pendown()
    if not lane: paint.forward(720)
    else: 
        for xcor in range(-360, 360, 40):
            if xcor % 80 == 0: paint.pendown()
            else: paint.penup()
            paint.forward(40)

def roadSetup():
    global road, paint
    road.tracer(0)
    road.listen()
    road.screensize(600,600)
    road.bgcolor("DarkSlateGray")
    paint.hideturtle()
    paint.color("Gainsboro")
    for ycor in range(210, -280, -70):
        if ycor == 0: drawRoad(position=(-360,ycor), line_width=DIVIDER, lane=False)
        elif ycor == 210 or ycor == -210: drawRoad(position=(-360,ycor), line_width=ROAD_BORDER, lane=False)
        else: drawRoad(position=(-360,ycor), line_width=LANE_LINE, lane=True)

road = Screen()
paint = Turtle()
roadSetup()

timmy = Player()
banner = Level()
road.onkey(lambda: timmy.forward(20), key="Up")
banner.display()

cars = []

gameisOn = True

while gameisOn and banner.level < 6: 
    sleep(0.04)
    if random.choice([True, False, False, False, False, False]) and len(cars) < 14+banner.level:
        lambo = Car()
        cars.append(lambo)
    for lambo in cars:
        lambo.speed(random.choice(speeds))
        lambo.forward(random.randint(5, 12))
        if timmy.distance(lambo.position()) < 25:
            timmy.shape("circle")
            timmy.shapesize(stretch_len=1.5, stretch_wid=0.8)
            timmy.color("red")
            gameisOn = False
            break
        (xcor, ycor) = lambo.position()
        if xcor < -340: lambo.resetCarPosition()
    if timmy.ycor() > 240: 
        timmy.goto(0, -250)
        banner.nextLevel()
        speeds.pop(0)
    road.update()

banner.display(gameisOn)
road.exitonclick()