from turtle import *

tracer(0)
right(180)
forward(5*15)
right(90)
forward(10*15)
right(90)
forward(5*15)
right(90)
for i in range(5):
    circle(5*15,180)

for x in range(-50, 50):
    for y in range(-50, 50):
        up()
        goto(x*15, y*15)
        down()
        dot(5)
done()