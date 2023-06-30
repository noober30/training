import tkinter as tk
import random

# Funkcia pre zafarbenie štvorca na náhodnú farbu
def color_square(event):
    x = event.x // 50  # Poradové číslo štvorca v rade
    y = event.y // 50  # Poradové číslo štvorca v stĺpci

    # Skontroluj, či event.y je v správnom intervale (vnútri štvorca)
    if y < 8:
        # Vygeneruj náhodnú farbu
        color = random.choice(['red', 'green', 'blue', 'yellow', 'purple', 'orange'])
        
        # Zafarbí kliknutý štvorec na vybranú farbu
        canvas.itemconfig(squares[x][y], fill=color)

# Vytvor okno
window = tk.Tk()
window.title("Vykresľovanie štvorcov")

# Vytvor plátno s veľkosťou pre 8 štvorcov veľkosti 50x50
canvas = tk.Canvas(window, width=400, height=50)

# Vytvor maticu na uchovávanie odkazov na štvorce
squares = [[None] * 8 for _ in range(8)]

# Vykresli 8 štvorcov vedľa seba
for x in range(8):
    for y in range(8):
        x1 = x * 50
        y1 = y * 50
        x2 = x1 + 50
        y2 = y1 + 50
        square = canvas.create_rectangle(x1, y1, x2, y2, fill='white')
        squares[x][y] = square

# Pripoj funkciu color_square k udalosti kliknutia myšou
canvas.bind("<Button-1>", color_square)

# Zobraz plátno
canvas.pack()

# Spusti hlavnú slučku udalostí
window.mainloop()
