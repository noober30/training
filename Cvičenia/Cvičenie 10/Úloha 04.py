import tkinter
import random

display_width = 640
display_height = 480

canvas = tkinter.Canvas(width=display_width, height=display_height)
canvas.pack()

def press(event):
    text = event.char
    positionx = random.randint(1,display_width-1)
    positiony = random.randint(1,display_height-1)
    canvas.create_text(positionx, positiony,text=text, font=("Arial",15))


canvas.bind_all("<Key>", press)


canvas.mainloop()