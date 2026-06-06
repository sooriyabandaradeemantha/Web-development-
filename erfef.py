import turtle


screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Turtle Shapes")

pen = turtle.Turtle()
pen.pensize(3)
pen.color("darkblue")


def draw_triangle():
    for _ in range(3):
        pen.forward(100)
        pen.left(120)


def draw_rectangle():
    for _ in range(2):
        pen.forward(150)
        pen.left(90)
        pen.forward(80)
        pen.left(90)

# Draw shapes
pen.penup()
pen.goto(-150, 0)
pen.pendown()
draw_triangle()

pen.penup()
pen.goto(100, 0)
pen.pendown()
draw_rectangle()


screen.mainloop()
