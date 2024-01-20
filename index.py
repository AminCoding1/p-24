import turtle
turtle.bgcolor("black")
t = turtle.Turtle()
screen = turtle.Screen()
t.pensize(4)
t.pencolor("white")
tri_arc_size = 250
number_of_tri_arcs = 6

def tri_arc(color, x):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(3):
        t.circle(x, 60)
        t.left(180)
    t.end_fill()

t.penup()
for color in ["green", "white"]:
    for i in range(number_of_tri_arcs):
        t.forward(0.05 * tri_arc_size)
        t.pendown()
        tri_arc(color, tri_arc_size)
        t.penup()
        t.backward(0.05 * tri_arc_size)
        t.left(360 / number_of_tri_arcs)
    tri_arc_size = 0.7 * tri_arc_size
    t.left(360 / (2 * number_of_tri_arcs))
t.hideturtle()
screen.exitonclick()
