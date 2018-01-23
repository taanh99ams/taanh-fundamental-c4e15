from turtle import *

shape("turtle")
speed(0)

listcolor = ["grey","yellow","brown","blue","red"]
x = 250

for i in listcolor:
    color(i)
    begin_fill()
    for j in range(5):
        for j in range(2):
            forward(x)
            left(90)
            forward(100)
            left(90)
    end_fill()
    x = x - 50



















mainloop()
