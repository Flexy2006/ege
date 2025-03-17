from turtle import *
tracer(0)
for i in range(5):
    forward(9*15)
    right(90)
    forward(3*15)
    right(90)
for x in range(-50,50):
    for y in range(-50,50):
        up()
        goto(x*15,y*15)
        down()
        dot(5)
done()