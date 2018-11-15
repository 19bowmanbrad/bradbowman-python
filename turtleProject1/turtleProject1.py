import turtle
turtle.setup(width=600, height=500)
screen = turtle.Screen()
turtle.title("Turtle Starter")
turtle.reset()
turtle.bgcolor('black')

def main():
    # color = input("choose a color")
    # sideLength = input("side length")
    # numSides = input("how many sides")
    # advancedShapes(str(color), int(sideLength), int(numSides))
    # advancedShapes((.4, .9, .6), 80, 7)
    screenSpace()

# Add your methods here
def draw():
    turtle.pencolor('cyan')
    turtle.goto(-50, 0)
    turtle.forward(100)
    turtle.penup()
    turtle.goto(0, -75)
    turtle.penup()
    turtle.goto(-100, -100)
    turtle.pendown()
    turtle.pencolor(0.5, 0.8, 0.3)
    for x in range(4):
        turtle.forward(200)
        turtle.left(90)
    turtle.penup()
    turtle.goto(0, -300)
    turtle.pendown()
    turtle.pencolor('#ffe063')
    turtle.circle(300) #circle goes off screen because the RADIUS  is 300, therefore the diameter is equal to the width and greater than the height.
    turtle.penup()
    turtle.goto(-200, -150 )
    turtle.pendown()
    for x in range(3):
        turtle.forward(400)
        turtle.left(120)

def advancedShapes(color, sideLength, numSides):
    turtle.penup()
    turtle.goto((-.5*sideLength), (-.75*sideLength))
    turtle.pencolor(color)
    turtle.pendown()
    turtle.speed(0)
    turtle.pensize()
    for x in range(numSides):
        turtle.forward(sideLength)
        turtle.left((360/numSides))
    turtle.penup()

def screenSpace():
    turtle.goto(150, 100)
    turtle.color('green')
    turtle.pendown()
    turtle.circle(50)
    turtle.penup()
    turtle.goto(-150, 100)
    turtle.pendown()
    turtle.color('white')
    turtle.circle(50)
    turtle.penup()
    turtle.goto(-150, -180)
    turtle.pendown()
    turtle.color('blue')
    turtle.circle(50)
    turtle.penup()
    turtle.goto(150, -180)
    turtle.pendown()
    turtle.color('yellow')
    turtle.circle(50)




# draw()
main()
# Allow screen exit on clicking window
turtle.exitonclick()
