import tkinter as tk
import random

def color_square(event):
    x = event.x // 50
    y = event.y // 50
    if 0 <= x < 8 and 0 <= y < 1:
        color = '#%06x' % random.randint(0, 0xFFFFFF)  # Generovanie náhodnej farby
        canvas.itemconfig(squares[x], fill=color)

root = tk.Tk()
canvas = tk.Canvas(root, width=640, height=480, bg='white')
canvas.pack()

squares = []
for i in range(8):
    x1 = i * 50
    y1 = 0
    x2 = x1 + 50
    y2 = y1 + 50
    square = canvas.create_rectangle(x1, y1, x2, y2, fill='white')
    squares.append(square)

canvas.bind('<Button-1>', color_square)
root.mainloop()
