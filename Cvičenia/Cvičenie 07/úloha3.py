#Napíš funkcie ball(x, y, r) a snowman(x, y, r). Funkcia ball() nakreslí biely kruh so stredom x, y 
#a s polomerom r. Funkcia snowman() pomocou troch volaní ball() nakreslí snehuliaka, v ktorom spodná 
#najväčšia guľa má stred (x, y) a polomer r. Stredná má polomer 2/3 veľkej a najmenšia je polovičná 
#strednej. Otestuj na bledomodrom pozadí. napr.

import tkinter


canvas = tkinter.Canvas(width=640, height=480)
canvas.configure(background="lightblue")
canvas.pack()

def ball(x, y, r):
    canvas.create_oval(x-r,y-r, x+r,y+r, fill="white")

def snowman():
    ball(centerx, centery,r )
    ball(centerx , centery - r*1.66, r*0.66)
    ball(centerx , centery - r*2.66, r*0.33)  

r = 80
centerx, centery = 320,300
snowman()

canvas.mainloop()