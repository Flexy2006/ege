from turtle import *
tracer(0)
for i in range(4):
    forward(8*15)
    right(90)
for i in range(3):
    forward(12*15)
    right(120)
for x in range(-20, 20):
    for y in range(-20, 20):
        up()
        goto(x*15, y*15)
        down()
        dot(5)
done()#43