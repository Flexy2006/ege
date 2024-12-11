from turtle import *
tracer(0)
for i in range(4):
    forward(12*15)
    right(90)
for j in range(5):
    forward(4*15)
    right(45)  
for x in range(-30, 30):
    for y in range(-30, 30):
        up()
        goto(x*15, y*15)
        down()
        dot(5)
done()