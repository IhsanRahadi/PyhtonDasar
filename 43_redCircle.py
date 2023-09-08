import turtle

# Set up the turtle screen and set the background color the white
screen = turtle.Screen ()
screen.bgcolor("white")

# Cratee a new turtle and set its speed to the fasttest possible
pen = turtle.Turtle ()
pen.speed(0)

# Set thr fill color to red
pen.fillcolor("red")
pen.begin_fill()

# Draw the circle with a radius of 100 pixels
pen.circle(100)

# End the fill and stop drawing
pen.end_fill()
pen.hideturtle()

# Keep the turtle window open until it is manually closed
turtle.done()