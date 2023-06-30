#V ploche sa nachádza jeden červený štvorček veľkosti 50x50. Keď klikneme do jeho vnútra 
#(počíta sa aj obvod), môžeme ho ťahať, teda posúvať po ploche podľa
#pohybu myši (inak ťahanie s kliknutím mimo štvorček nerobí nič).

import tkinter
screen_width = 640
screen_height = 480

canvas = tkinter.Canvas(width=screen_width, height=screen_height)
canvas.pack()



canvas.create_rectangle(300,300,250,250, fill="red" )
rect_id = (300,300,250,250)

def presun(event):
    event.x 
    
    
canvas.mainloop()