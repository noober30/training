import tkinter

screen_width = 1280
screen_height = 960
canvas = tkinter.Canvas(width=screen_width, height=screen_height)
canvas.pack()

r = 50
oval_id = canvas.create_rectangle(screen_width/2-r,
                                screen_height/2-r, 
                                screen_width/2+r, 
                                screen_height/2+r, 
                                fill="red")

smer = -1                                       #tento pohyb nahor cez -1 ma odjebal, magic
is_moving = False

def pohyb():
    global smer, is_moving
    x1, y1, _, _ = canvas.coords(oval_id)        #s čiastkovými poroblémami mi musel pomôcť chatGPT
    if y1 + r + 300 >= screen_height:
        smer = -1
    elif y1 <= 0:
        smer = 1
    canvas.move(oval_id, 0, smer * 5)
    if is_moving:
        canvas.after(10, pohyb)

def start_stop(event):
    global is_moving
    is_moving = not is_moving
    if is_moving:
        pohyb()

canvas.bind_all("<ButtonPress-1>", start_stop)

canvas.mainloop()

