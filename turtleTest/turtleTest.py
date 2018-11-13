import turtle

def main():
    draw = turtle.Pen()
    turtle.bgcolor("cyan")
    draw.speed(.25)
    for x in range (2):
        for i in range (0, 4):
            draw.forward(100)
            draw.left(90)
        draw.penup()
        draw.goto(-150, 0)
        draw.pendown()
    draw.penup()
    draw.goto(-250, -200)
    draw.pendown()
    for x in range (2):
        for i in range (0, 2):
            draw.forward(250)
            draw.left(90)
            draw.forward(50)
            draw.left(90)
        draw.penup()
        draw.goto(30, -200)
        draw.pendown()
    draw.pencolor("white")
    draw.penup()
    draw.goto(0, 200)
    draw.pendown()
    for x in range(100):
        draw.forward(x)
        draw.left(91)
    draw.hideturtle()
    input()


main()
