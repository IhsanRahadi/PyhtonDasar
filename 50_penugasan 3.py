import turtle

def drawRectangle(ttl, x, y, width, height, color):
    ttl.penup()
    ttl.goto(x, y)
    ttl.pendown()
    ttl.color(color)
    ttl.begin_fill()
    for count in range(2):
        ttl.forward(width)
        ttl.left(90)
        ttl.forward(height)
        ttl.left(90)
    ttl.end_fill()
    ttl.penup()

def drawFlag():
    window = turtle.Screen()
    window.bgcolor("black")

    bob = turtle.Turtle()
    bob.speed(10)
    bob.pensize(3)
    drawRectangle(bob, -150, 100, 450, 200, "red")
    drawRectangle(bob, -150, -100, 450, 200, "white")

    turtle.done()

drawFlag()