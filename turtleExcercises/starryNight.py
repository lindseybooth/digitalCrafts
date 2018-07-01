from turtle import *

bgcolor("black")

color("white")

#Star1
begin_fill()
for i in range(5):
    forward(110)
    right(216)
end_fill()
penup()

#Star2
begin_fill()
goto(-120, 120)
pendown()
for i in range(5):
    forward(100)
    right(144)
end_fill()
penup()

#Star3
begin_fill()
goto(250, 250)
pendown()
for i in range(5):
    forward(110)
    right(216)
end_fill()
penup()

#Star4
begin_fill()
goto(-250, -275)
pendown()
for i in range(5):
    forward(100)
    right(144)
end_fill()
penup()

#Star5
begin_fill()
goto(-250, 250)
pendown()
for i in range(5):
    forward(110)
    right(216)
end_fill()
penup()

#Star6
begin_fill()
goto(120, -120)
pendown()
for i in range(5):
    forward(100)
    right(144)
end_fill()
penup()

#Star7

begin_fill()
goto(50, 150)
pendown()
for i in range(5):
    forward(110)
    right(216)
end_fill()
penup()

#Star8
begin_fill()
goto(90, 90)
pendown()
for i in range(5):
    forward(100)
    right(144)
end_fill()
penup()

#Star9
begin_fill()
goto(-200, -100)
pendown()
for i in range(5):
    forward(110)
    right(216)
end_fill()
penup()

#Star10
begin_fill()
goto(-275, 60)
pendown()
for i in range(5):
    forward(100)
    right(144)
end_fill()
penup()

mainloop()
