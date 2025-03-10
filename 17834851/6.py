from turtle import *
tracer(0)
for i in range(9):
    forward(22*15)
    right(90)
    forward(6*15)
    right(90)
up()
forward(1*15)
right(90)
forward(5*15)
left(90)
down()
for i in range(9):
    forward(53*15)
    right(90)
    forward(75*15)
    right(90)
for x in range(-25, 25):
    for y in range(0, 100):
        up()
        goto(x*15, y*15)
        down()
        dot(3)
done()