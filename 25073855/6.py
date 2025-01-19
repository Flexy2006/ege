from turtle import *
tracer(0)
for i in range(8):
    forward(16*15)
    right(90)
    forward(22*15)
    right(90)
up()
forward(5*15)
right(90)
forward(5*15)
left(90)
down()
for m in range(8):
    forward(52*15)
    right(90)
    forward(77*15)
    right(90)
for x in range(-30, 30):
    for y in range(-30, 30):
        up()
        goto(x*15, y*15)
        down()
        dot(5)
done()