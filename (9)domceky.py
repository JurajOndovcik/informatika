import tkinter
import random

canvas = tkinter.Canvas(width=600, height=600)
canvas.pack()

x0 = 50
y0 = 150

def dom(x, y, vel1, vel2):
    infill = random.choice(("red", "blue", "green", "cyan", "orange"))
    infill2 = random.choice(("red", "blue", "green", "cyan", "orange"))
    canvas.create_rectangle(x,y-vel1,x+vel1,y,fill=infill)
    canvas.create_polygon(x,y-vel1,x+vel1,y-vel1,x+(vel1/2), y-vel1-vel2, fill=infill2, outline='black')

while x0 <= 550:
    v = random.randint(10,50)

    dom(x0, y0, v, random.randint(10,50))
    x0 += v

canvas.mainloop()
