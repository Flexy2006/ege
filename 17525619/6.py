from turtle import *
tracer(0)
for i in range(4):
    forward(6*15)
    right(150)
    forward(6*15)
    right(30)
for x in range(-50,50):
    for y in range(-50, 50):
        up()
        goto(x*15, y*15)
        down()
        dot(5)
done()