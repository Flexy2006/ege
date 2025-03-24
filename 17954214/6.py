from turtle import *
tracer(0)
right(180)
forward(2*8)
right(90)
forward(40*8)
right(90)
forward(2*8)
for i in range(4):
    circle(-5*8, 180)
    right(180)
for x in range(-50,50):
    for y in range(-50, 50):
        up()
        goto(x*8, y*8)
        down()
        dot(3)
done()