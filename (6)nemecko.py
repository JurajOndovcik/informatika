import tkinter
import random

canvas = tkinter.Canvas(width=400, height=300, background='white')
canvas.pack()

for i in range(10000):
    x = random.randint(10,350)
    y = random.randint(10,250)

    if y < 90:
        color = 'black'
    elif y >= 90 and y <= 170:
        color = 'red'
    elif y > 170:
        color = 'gold'

    canvas.create_oval(x,y,x+10,y+10,fill=color,outline=color)
    

canvas.mainloop()