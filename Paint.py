"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""


import math
from turtle import *

from freegames import vector
from numpy import sqrt


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    fillcolor(color)
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    """Se dibuja un ciruclo de principio a fin"""
    up()

    """El radio sera la distancia entre los dos puntos, inicio y final, se obtiene usando la siguiente formula:"""
    radius = sqrt(round(end.x-start.x) ^ 2)+(round(end.y - start.y) ^ 2)

    """Steps sera la cantidad de vultas hacia la derecha que dara Turtle para dar la ilusión de dar vuelta en circulo, deberia ser 360 pero va muy lento"""
    steps = 20

    """Extent sirve para formar la vuelta enter, debe ser 360, si es menor a 360, el circulo queda incompleto, si es mayor a 360 da un ciruclo entero y más"""
    extent = 360

    """Theta sirve para encontrar la distancia en linea recta que debe seguir Turtle antes de dar vuelta a la derecha."""
    theta = extent/steps
    step_size = 2*radius*math.sin(math.radians(theta/2))

    goto(start.x, start.y)
    down()
    left(theta/2)
    fillcolor()
    begin_fill()
    for i in range(1, steps):
        left(theta)
        forward(step_size)
    left(theta/2)
    end_fill()


def rectangle(start, end):
    """Draw rectangle from start to end."""
    pass  # TODO


def triangle(start, end):
    """Draw triangle from start to end."""
    pass  # TODO


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')

"""Se agrego el color de relleno amarillo y se selecciona con la letra mayuscula Y"""
onkey(lambda: color('yellow'), 'Y')

onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
