"""
Do plochy nakresli tesne vedľa seba 8 štvorcov veľkosti 50x50. Na každé kliknutie sa príslušný 
kliknutý štvorec zafarbí na červeno (alebo na nejakú náhodnú farbu). Poradové číslo štvorca v rade 
zistíš z x-ovej súradnice kliknutého bodu event.x // 50. Skontroluj, či aj event.y je v správnom 
intervale, t. j. kliklo sa do vnútra niektorého štvorca a nie niekde mimo.
"""

import tkinter

canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()

def rectangles(x1,y1, x2, y2):
    id = []
    for i in range(1,9):
        rect = canvas.create_rectangle(x1,y1, x2,y2)
        canvas.create_text(x1+25,y1+25, text="{}".format(i))
        id.append(rect)
        x1+= 50
        x2+= 50
    print( id)



x = 0
y = 50     
id_1 = 0,0,50,50


def click (event):
    if event.x < 50 and event.y < 50:
        canvas.config(id_1, fill ="Red")
        print("yes")
    

canvas.bind_all("<Button-1>", click)                                                           



rectangles(2, 2, 52, 52)
canvas.mainloop()
"""
def spracuj_udalost(event):
    coordinates = f"({event.x}, {event.y})"
    canvas.create_text(event.x, event.y, text = coordinates, font=("Arial",25))
    if event.x and event.y in range( id_1):
        pass
"""