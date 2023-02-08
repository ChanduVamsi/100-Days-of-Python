# More into state and instances of the same object - Turtle

import os, random
from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("LavenderBlush")
screen.setup(width=1000, height=800)
screen.title(titlestring="Welcome to the turtle race!")
user_choice = screen.textinput(title="Which turtle will win the race?", prompt="Enter colour (red/orange/Goldenrod/green/blue/purple): ").lower()

all_turtles = []
colors = ['red', 'orange', 'Goldenrod', 'green', 'blue', 'purple']
ycor = 175

for turtle_index in range(6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color('black', colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -450, y = ycor)
    new_turtle.pensize(5)
    new_turtle.pencolor(colors[turtle_index])
    all_turtles.append(new_turtle)
    ycor -= 50

if user_choice != "": on_game = True

while on_game:
    for turtle_player in all_turtles:
        if turtle_player.xcor() > 470:
            winner = turtle_player.color()[0].lower()
            on_game = False
            break
        turtle_player.forward(random.randint(1,13))
screen.exitonclick()

os.system("clear")
if user_choice == winner: print("\nCongratulations! You won the bet 🥳\n")
else: print(f"\nThe winner is {winner}. You lost the bet 😭\n")