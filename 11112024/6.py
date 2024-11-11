from turtle import *
tracer(0)
for i in range(6):
    forward(13*15)
    right(120)
for x in range(-20, 20):
    for y in range(-20, 20):
        up()
        goto(x*15, y*15)
        down()
        dot(5)
done()#43