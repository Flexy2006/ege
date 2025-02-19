from turtle import *

tracer(0)
for i in range(2):
    forward(15*15)
    right(90)
    forward(8*15)
    right(90)


for x in range(-25, 25):
    for y in range(-25, 25):
        up()
        goto(x*15, y*15)
        down()
        dot(5)
done()