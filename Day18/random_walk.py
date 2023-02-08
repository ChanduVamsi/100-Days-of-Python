import turtle, random
# from turtle import Turtle as T, Screen as S

tim = turtle.Turtle()
turtle.colormode(255)

# east - 0, north - 90, west - 180, south - 270
directions = [0, 90, 180, 270]

# colors = ['black','peru','red','orange','gold','cyan','teal','chartreuse','lavender','coral']
tim.pensize(12)
tim.speed(0)

for _ in range(300):
    tim.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    tim.setheading(random.choice(directions))
    tim.forward(30)

canvas = turtle.Screen()
canvas.exitonclick()