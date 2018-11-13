import turtle
turtle.setup(width=600, height=500)
screen = turtle.Screen()
turtle.title("Turtle Starter")
turtle.reset()
turtle.bgcolor('black')

# Add your methods here
def draw():
    turtle.pencolor('white')
    turtle.goto(-50, 0)
    turtle.forward(100)
    turtle.penup()
    turtle.goto(0, -75)
    turtle.penup()
    turtle.goto(-100, -100)
    turtle.pendown()
    for x in range(4):
        turtle.forward(200)
        turtle.left(90)
    turtle.penup()
    turtle.goto(0, -300)
    turtle.pendown()
    turtle.circle(300) #circle goes off screen because the RADIUS  is 300, therefore the diameter is equal to the width and greater than the height.

# Kick off drawing
draw()

# Allow screen exit on clicking window
turtle.exitonclick()
