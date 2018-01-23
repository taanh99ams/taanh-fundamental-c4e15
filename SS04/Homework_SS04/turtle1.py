from turtle import *

shape("turtle")
speed(0)

listcolor = ["red","blue","purple","yellow","grey"]

x = 3

for i in listcolor:
    color(i)
    for j in range(x):
        forward(100)
        left(360 / x)
    x += 1










mainloop()
