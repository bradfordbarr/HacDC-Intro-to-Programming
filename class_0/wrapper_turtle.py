import turtle

"""
Simple turtle graphics abstractions
"""

T = turtle.Turtle()

def forward(n):
    """
    Go forward n units
    """
    T.forward(n)

def backward(n):
    """
    Go backward n units
    """
    T.backward(n)

def left(n):
    """
    Turn left n degrees
    """
    T.left(n)

def right(n):
    """
    Turn right n degrees
    """
    T.right(n)

def penup():
    """
    Lift pen
    """
    T.penup()

def pendown():
    """
    Put pen down
    """
    T.pendown()

def done():
    """
    Keeps the display open until the user closes it or the program is killed
    """
    turtle.done()
