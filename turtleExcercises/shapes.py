from turtle import *

def triangle():
    forward(100)
    right(120)
    forward(100)
    right(120)
    forward(100)
    right(120)
    
    mainloop()

def square():
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    
    mainloop()

def pentagon():
    forward(100)
    right(72)
    forward(100)
    right(72)
    forward(100)
    right(72)
    forward(100)
    right(72)
    forward(100)
    right(72)
    mainloop()

def hexagon():
    forward(100)
    right(-60)
    forward(100)
    right(-60)
    forward(100)
    right(-60)
    forward(100)
    right(-60)
    forward(100)
    right(-60)
    forward(100)
    right(-60)
    
    mainloop()

def octogon():
    forward(100)
    right(-45)
    forward(100)
    right(-45)
    forward(100)
    right(-45)
    forward(100)
    right(-45)
    forward(100)
    right(-45)
    forward(100)
    right(-45)
    forward(100)
    right(-45)
    forward(100)
    right(-45)

    mainloop()

def star():
    for i in range(5):
        forward(100)
        right(144)
    
    mainloop()

def circle():
    penup()
    forward(50)
    left(90)
    forward(50)
    left(90)
    pendown()

    width(2)
    circle(180)

    mainloop()

