from turtle import *
tracer(0)
for i in range(6):
    forward(10*10)
    right(60)
for x in range(-20, 20):
    for y in range(-20, 20):
        up()
        goto(x*10, y*10)
        down()
        dot(3)
done()#269?