# Replicating a digital art by Damien Hirst - The Complete Spot Paintings

import turtle, colorgram, random
turtle.colormode(255)

colours = colorgram.extract('Day18/image.jpg', 50)

art = turtle.Turtle()
canvas = turtle.Screen()

art.speed(0)
art.penup()

art.setheading(150)
art.forward(760)
art.setheading(0)

for __ in range(16):
    for _ in range(27): 
        colour = random.choice(colours)
        art.dot(20, (colour.rgb.r, colour.rgb.g, colour.rgb.b))
        art.forward(50)
    art.setheading(270)
    art.forward(50)
    art.setheading(180)
    art.forward(1350)
    art.setheading(0)
    art.hideturtle()

canvas.exitonclick()