from turtle import *

def draw_square(length, colour):
    speed(0)
    color(colour)
    shape("turtle")
    for i in range(4):
        forward(length)
        left(90)

# draw_square(100, "red")
