from turtle import *

def draw_star(x,y,length):
    angle = 144
    left(108)
    for i in range(5):
        left(angle)
        forward(length)

draw_star(100,150,100)

mainloop()
