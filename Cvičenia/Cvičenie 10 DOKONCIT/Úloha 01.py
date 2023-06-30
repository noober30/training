import tkinter

canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()


def spracuj_udalost(event):                                 
    coordinates = f"({event.x}, {event.y})"
    canvas.create_text(event.x, event.y, text = coordinates, font=("Arial",5))               
                                                                   
canvas.bind_all("<ButtonPress-1>", spracuj_udalost)


canvas.mainloop()