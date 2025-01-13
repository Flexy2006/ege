from turtle import *
tracer(0)
for i in range(2):
    forward(20*15)
    right(90)
    forward(9*15)
    right(90)
left(90)
for i in range(2):
    forward(20*15)
    right(90)
    forward(9*15)
    right(90)
for x in range(-30, 30):
    for y in range(-30, 30):
        up()
        goto(x*15, y*15)
        down()
        dot(5)
done()