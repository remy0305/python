import turtle
import random
c = turtle.Turtle()
c.speed(30)

for i in range(1,6):
    for j in range(-2,3 - i+1):
        c.penup()
        if random.choice([True,False]):
            c.goto(-500+i*150+50,j*150)
            color=(random.random(),random.random(),random.random())
            c.color(color)
            c.pendown()
            c.begin_fill()
            c.circle(50)
            c.end_fill()
            c.penup()
            continue
        else:
            color=(random.random(),random.random(),random.random())
            c.goto(-500+i*150,j*150)
            c.pendown()
            c.color(color)
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
            
input("Hit enter.")