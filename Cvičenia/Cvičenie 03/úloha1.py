import tkinter

canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()

r = int(input("Zadaj priemer stvorca : "))
centerx, centery = 320, 240



center = (centerx-r,centery-r,centerx+r,centery+r)
downright_id = centerx,centery,centerx+(r*2), centery+(r*2)
upperright_id = (centerx+(r*2), centery-(r*2), centerx, centery)
upperleft_id = centerx-(r*2), centery-(r*2), centerx, centery
downleft_id = (centerx,centery,centerx-(r*2), centery+(r*2))
middleright_id = (centerx,centery-r, centerx+r*2,centery+r)
middleleft_id = (centerx-r*2,centery-r, centerx,centery+r)
middleup_id = (centerx-r,centery-r*2,centerx+r,centery)
middledown_id = (centerx-r,centery, centerx+r,centery+r*2)


canvas.create_oval(center)
canvas.create_oval(downright_id)
canvas.create_oval(upperleft_id)
canvas.create_oval(upperright_id)
canvas.create_oval(downleft_id)
canvas.create_oval(middleright_id)
canvas.create_oval(middleleft_id)
canvas.create_oval(middleup_id)
canvas.create_oval(middledown_id)

canvas.mainloop()