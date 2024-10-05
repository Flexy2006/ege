from turtle import *
tracer(0)
left(45)
for i in range(7):
    forward(5 * 10)
    right(45)
    forward(10 * 10)
    right(135)
for x in range(0, 15):
    for y in range(0, 15):
        up()
        goto(x*10, y*10)
        down()
        dot(5)
done()#27