import tkinter
import datetime

canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()


def tik():
    current = datetime.datetime.now()
    timestring = current.strftime("%H:%M:%S.")+ str(current.microsecond//100000)
    canvas.itemconfig("time_text", text = timestring)
    canvas.create_text(320, 240, text=timestring,font=("Arial", 50), tags = "time_text")
    canvas.after(100,tik)


tik()


canvas.mainloop()

