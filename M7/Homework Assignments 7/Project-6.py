import turtle

screen = turtle.Screen()
screen.bgcolor("blue")

t = turtle.Turtle()
t.color("green")    
t.fillcolor("green") 
t.speed("fast")         
t.hideturtle()

t.penup()
t.goto(-200, 0)
t.pendown()

t.begin_fill()
for _ in range(3):
    t.forward(100)
    t.left(120)
t.end_fill()

t.penup()
t.color("orange")
t.goto(0, 0) 
t.setheading(0)
t.pendown()

t.begin_fill()
for _ in range(2):
    t.forward(150)
    t.left(90)
    t.forward(80)
    t.left(90)
t.end_fill()

t.penup()
t.color("red")
t.goto(250, 0) 
t.setheading(0)
t.pendown()

t.begin_fill()
for _ in range(6):
    t.forward(70)
    t.left(60)
t.end_fill()

turtle.done()