import tkinter
canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()

r = int(input("Zadaj polomer kruhov v pixeloch : "))
x1, y1 = int(input("Zadaj súradnice x prvého bodu : ")), int(input("Zadaj súradnice y prvého bodu : "))
x2, y2 = x1+r, x1 +r

blue_id = (x1,y1,x1+r, y1+r)
black_id = (x1+r*1.02,y1,x2+r, y2)
red_id = (x1+r*2.02,y1, x2+r*2.02, y2,)                 #moc zlozita matematika ale funguje to
yellow_id = (x1+r*1.5,y1+r*1.5, x2-r/2,y2-r/2)
green_id = (x1+r*1.52,y1+r*1.5,x2+r*1.5,y2-r/2)


canvas.create_oval(blue_id, outline="blue")
canvas.create_oval(black_id)
canvas.create_oval(red_id, outline= "red")
canvas.create_oval(yellow_id, outline="yellow")
canvas.create_oval(green_id, outline = "green")


canvas.mainloop()