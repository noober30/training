import tkinter

screen_width = 640
screen_height = 480

canvas = tkinter.Canvas(width=screen_width, height=screen_height)
canvas.pack()

rect_id = canvas.create_rectangle(300, 300, 250, 250, fill="red")
startx, starty = 0, 0
moving = False

def click(event):
    global startx, starty, moving
    item = canvas.find_overlapping(event.x, event.y, event.x, event.y)
    if item and item[0] == rect_id:
        startx, starty = event.x, event.y
        moving = True

def drag(event):
    global moving, startx, starty
    if moving:
        endx, endy = event.x - startx, event.y - starty
        canvas.move(rect_id, endx, endy)
        startx, starty = event.x, event.y

def release(event):
    global moving
    moving = False


canvas.bind_all("<ButtonPress-1>", click)
canvas.bind_all("<B1-Motion>", drag)
canvas.bind_all("<ButtonRelease-1>", release)
canvas.mainloop()
