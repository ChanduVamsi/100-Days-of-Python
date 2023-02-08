#Event listeners, higher order functions - more about turtle

from turtle import Turtle, Screen

def move_forward(): tim.forward(10)
def move_backward(): tim.backward(10)
def rotate_clockwise(): tim.right(10)
def rotate_anticlockwise(): tim.left(10)
def clear_drawing(): tim.reset()

tim = Turtle()
canvas = Screen()

canvas.listen()
canvas.onkey(key="w", fun=move_forward)
canvas.onkey(key="s", fun=move_backward)
canvas.onkey(key="a", fun=rotate_clockwise)
canvas.onkey(key="d", fun=rotate_anticlockwise)
canvas.onkey(key="c", fun=clear_drawing)
canvas.exitonclick()