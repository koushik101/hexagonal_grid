import collections
import math
import turtle

SIZE = 1
COOD = 80

Point = collections.namedtuple("Point", ["x", "y"])
Hex = collections.namedtuple("Hex", ["q", "r"])

def hex_to_pixel(hex):
    x = SIZE * math.sqrt(3) * (hex.q + hex.r/2)
    y = SIZE * 3/2 * hex.r
    return Point(x, y)

sc=turtle.Screen()
tr=turtle.Turtle()

def init_turtle():
    tr.hideturtle()
    sc.bgcolor("lightgreen")
    sc.title("Hex")
    tr.color("blue")
    tr.pensize(1)
    tr.fillcolor('red')

def draw_hex(hex, fill):
    tr.penup()
    tr.seth(0)
    tr.setpos(hex_to_pixel(hex))
    tr.forward(SIZE)
    tr.left(90)
    tr.pendown()
    if fill:
        tr.begin_fill()
    for i in range(6):
        tr.forward(SIZE);
        tr.left(60)
    if fill:
        tr.end_fill()

def draw_hexgrid():
    sc.tracer(0, 0)
    for i in range(-COOD, COOD):
            for j in range(-COOD, COOD):
                        draw_hex(Hex(i, j), False)
    sc.update()
    sc.tracer(4,20)

def draw_param_circle(x, y, r):
    for i in range(360):
        tx=int(2*r*(math.sin(math.radians(i+120)))/math.sqrt(3))
        ty=int(2*r*(math.sin(math.radians(i)))/math.sqrt(3))
        draw_hex(Hex(tx, ty), True)


init_turtle()
draw_hexgrid()
draw_param_circle(0, 0, 35)
sc.mainloop()
