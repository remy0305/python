import turtle
c = turtle.Turtle()
for i in range(1,6):
    for j in range(-2,3-i+1):
        c.penup()
        c.goto(-500+i*150,j*150)
        c.pendown()
        c.color("red")
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