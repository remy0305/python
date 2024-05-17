#用彩色三角形，和正方形畫三角形
import turtle
import random  
def spuare(c):
    c.begin_fill()
    c.forward(100)
    c.left(90)
    c.forward(100)
    c.left(90)
    c.forward(100)
    c.left(90)
    c.forward(100)
    c.left(90)
    c.end_fill()

c = turtle.Turtle()
c.speed(25)
for i in range(1,6):
    for j in range(-2,3-i+1): 
        if random .choice([True,False]):
            c.penup()
            color=(random .random(),random .random(),random .random())
            c.color(color)
            c.goto(-500+i*170,j*150)
            c.pendown
            c.begin_fill()
            c.circle(50)
            c.end_fill()
            continue
        else :
            c.penup()
            color=(random .random(),random .random(),random .random())
            c.color(color)
            c.goto(-500+i*150,j*150)
            c.pendown()
            spuare(c)
            