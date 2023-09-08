import turtle

def draw_rectangle(width, height):
    for count in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

def draw_triangle(side_length):
    for count in range(3):
        turtle.forward(side_length)
        turtle.left(120)

def draw_trapezium(base1, base2, height):
    turtle.forward(base1)
    turtle.left(135)
    turtle.forward(height)
    turtle.left(45)
    turtle.forward(base2)
    turtle.left(45)  
    turtle.forward(height)
    turtle.left(135)  
    turtle.forward(base1)
    turtle.forward(base2)

def draw_parallelogram(base, height):
    turtle.forward(base)
    turtle.left(60)
    turtle.forward(height)
    turtle.left(120)
    turtle.forward(base)
    turtle.left(60)
    turtle.forward(height)

def draw_rhombus(side_length):
    for count in range(2):
        turtle.forward(side_length)
        turtle.left(60)
        turtle.forward(side_length)
        turtle.left(120)

turtle.speed(5)

draw_rectangle(100, 50)

turtle.penup()
turtle.goto(150, 0)
turtle.pendown()


draw_triangle(100)

turtle.penup()
turtle.goto(-150, -100)
turtle.pendown()

draw_trapezium(100, 100, 80)

turtle.penup()
turtle.goto(150, -100)
turtle.pendown()

draw_parallelogram(100, 50)

turtle.penup()
turtle.goto(-150, -200)
turtle.pendown()

draw_rhombus(70)

turtle.exitonclick()