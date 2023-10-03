import tkinter
import random
import time

canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()

r = int(input("Zadaj polomer kruhu : ")) 
interval = int(input("Zadaj časový interval v milisekundách : "))

circle_ids = []
display_counter = 0
start_time = 0
fastest = []

def circle():
    global circle_ids, start_time
    centerx, centery = random.randint(1 + r * 2, 640) - r, random.randint(1 + r * 2, 480) - r
    suradnice = centerx - r, centery - r, centerx + r, centery + r
    canvas.delete("circle")
    canvas.create_oval(suradnice, fill="red", tags="circle")
    if circle_ids and circle_ids[0] in circle_ids:
        circle_ids.pop(0)
    circle_ids.append(suradnice)
    start_time = time.time()
    canvas.after(interval, circle)

def click(event):
    global circle_ids, display_counter, start_time
    x, y = event.x, event.y
    for suradnice in circle_ids:
        center_x = (suradnice[0] + suradnice[2]) / 2                        # s týmto mi pomohol chatGPT,
        center_y = (suradnice[1] + suradnice[3]) / 2                        # vedel som vypočítať len 
        distance = ((x - center_x) ** 2 + (y - center_y) ** 2) ** 0.5       # štvorec
        elapsed_time = time.time() - start_time
        if distance <= r:
            display_counter += 1
            canvas.delete("display")
            canvas.delete("timer")
            fastest.append(elapsed_time)
        else:
            display_counter -= 1
            canvas.delete("display")
            canvas.delete("timer")

def counter():
    global display_counter, fastest
    canvas.create_text(550, 20, text="Counter: {i}".format(i=display_counter), font=("Arial", 15), tag="display")
    elapsed_time = time.time() - start_time
    timer_text = "Time elapsed: {:.3f} sec".format(elapsed_time)
    if len(fastest) > 0:
        min_time = min(fastest)
        canvas.delete("best")
        canvas.create_text(550,60, text="Best: {:.3f}".format(min_time), font= ("Arial", 15), tag = "best")
    if canvas.find_withtag("timer"):
        canvas.itemconfig("timer", text=timer_text)
        
    else:
        canvas.create_text(530, 40, text=timer_text, font=("Arial", 15), tag="timer")
    canvas.after(100, counter)

canvas.bind_all("<ButtonPress-1>", click)

counter()
circle()

canvas.mainloop()


