#!/usr/bin/env python3.11.1
# Turtle Documentation: https://docs.python.org/3/library/turtle.html?highlight=turtle#module-turtle

from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color('black', 'white')
timmy.speed(0)
for _ in range(400):
    timmy.left(1.25)
    timmy.circle(500)
print(timmy)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()