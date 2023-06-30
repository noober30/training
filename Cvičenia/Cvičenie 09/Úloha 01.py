import turtle

tur=turtle.Turtle()

def stvorec (strana):
    for i in range(4):
        tur.lt(90)
        tur.fd(strana)
    tur.lt(90)
    tur.fd(strana)
           
def trojuholnik(strana):
    tur.lt(90)
    tur.fd(strana)
    tur.rt(120)
    tur.fd(strana)
    tur.rt(120)
    tur.fd(strana)

def domcek(strana, farba1, farba2):
    farba1 = tur.color(farba1)
    stvorec(strana)
    farba2 = tur.color(farba2)
    trojuholnik(strana)

domcek(50, "red", "green")

turtle.exitonclick()





