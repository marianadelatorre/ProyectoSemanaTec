"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *

from freegames import vector


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
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

#Se realizó la función para dibujar un circulo utilizando la letra "c" 

def draw_circle(start, end):
    """Draw circle with given start and end points."""
    radius = ((end.x - start.x) * 2 + (end.y - start.y) * 2) ** 0.5 
    center_x = (start.x + end.x) / 2  
    center_y = (start.y + end.y) / 2  

    up()
    goto(center_x, center_y - radius)
    down()
    begin_fill()
    circle(radius)
    end_fill()

#aqui, basandome en la logica de como realizar el cuadrado en la parte de arriba, cambie la logica para que cambie a rectangulo. 
def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for _ in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)
    end_fill()
    	

#aqui, basandome en la logica de como realizar el cuadrado en la parte de arriba, cambie la logica para que cambie a triangulo.
def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    side_length = ((end.x - start.x)**2 + (end.y - start.y) ** 2) ** 0.5
    for _ in range(3):
        forward(side_length)
        left(120)
    end_fill()


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

#Se agregó el color morado con la letra "P"
onkey(lambda: color('purple'), 'P')

onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape',draw_circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
