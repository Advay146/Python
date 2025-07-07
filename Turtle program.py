import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue") 

pen = turtle.Turtle()
pen.speed(3)

def draw_shape(sides, length, color):
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(sides):
        pen.forward(length)
        pen.left(360 / sides)
    pen.end_fill()
#Triangel
pen.penup()
pen.goto(-150, 0)
pen.pendown()
draw_shape(3, 100, "yellow")

# Hexagon
pen.penup()
pen.goto(50, 0)
pen.pendown()
draw_shape(6, 60, "green")

# Rectangle
pen.penup()
pen.goto(-50, -150)
pen.pendown()
pen.fillcolor("red")
pen.begin_fill()
for _ in range(2):
    pen.forward(120)
    pen.left(90)
    pen.forward(60)
    pen.left(90)
pen.end_fill()

pen.hideturtle()
screen.mainloop()