#!/usr/bin/env python3.11.1
# Turtle Documentation: https://docs.python.org/3/library/turtle.html?highlight=turtle#module-turtle

import turtle, random
turtle.colormode(255)

def spirograph():
    timmy.shape("turtle")
    timmy.color('black', 'white')
    for _ in range(160):
        # timmy.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 'white')
        timmy.left(2.25)
        timmy.circle(100)

def sharingan():
    canvas.bgcolor('red')
    timmy.shape("arrow")
    timmy.color('black')
    for _ in range(320):
        timmy.left(1.125)
        timmy.circle(130)

def macaroni():
    canvas.bgcolor('brown')
    timmy.shape("arrow")
    timmy.pensize(1)
    timmy.left(25)
    timmy.hideturtle()
    timmy.color('yellow')
    for _ in range(180):
        timmy.left(1.125)
        timmy.circle(130)
        timmy.backward(0.7)

timmy = turtle.Turtle()
timmy.speed(0)

canvas = turtle.Screen()

spirograph()
timmy.clear()

sharingan()
timmy.clear()

macaroni()

canvas.exitonclick()