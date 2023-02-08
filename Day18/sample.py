from turtle import Turtle, Screen

def dashed_line():
    for _ in range(10):
        tim.penup()
        tim.forward(5)
        tim.pendown()
        tim.forward(5)

tim = Turtle()
tim.shape("turtle")
tim.color("black","white")
tim.speed(0)
colors = ['black','peru','red','orange','gold','cyan','teal','chartreuse','lavender','coral']
for sides in range(3,12):
    tim.pencolor(colors[sides - 3])
    for iterations in range(sides):
        tim.forward(100)
        # dashed_line()
        tim.right(360/sides)

canvas = Screen()
canvas.exitonclick()