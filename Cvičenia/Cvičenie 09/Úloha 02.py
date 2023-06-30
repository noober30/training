import turtle
import random

t = turtle.Turtle()
turtle.delay(0)

def ulica(pole):
    for i in pole:
        domcek(i)
    t.pu()
    t.lt(90)
    t.fd(i)
    t.pd()

def domcek(strana):
    color = (random.random(), random.random(), random.random())
    t.color(color)
    for i in range(6):
        t.fd(strana)
        t.lt(90)
    color = (random.random(), random.random(), random.random())
    t.color(color)
    t.fd(strana)
    t.rt(120)
    t.fd(strana)
    t.rt(120)
    t.fd(strana)
    t.rt(30)
    t.pu()
    t.fd(strana)
    t.pd()
    t.lt(90)
   
t.pu()
t.goto(-300,-30)
t.pd()
ulica([60, 70, 40, 50, 20, 100])

turtle.exitonclick()