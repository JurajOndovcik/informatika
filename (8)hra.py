import tkinter
import random

k = int(input('Zadaj počet: '))

canvas = tkinter.Canvas(width=600,height=600)
canvas.pack()

def circle(x0,y0):
    global circles
    global sucet
    n = random.randint(1,4)
    sucet += n
    canvas.create_oval(x0,y0,x0+20,y0+20,)
    canvas.create_text(x0+10,y0+10,text=n)

y = 50

for i in range(10):
    sucet = 0
    x = 50

    while sucet < k:
        circle(x,y,)
        x += 30
    if sucet == k:
        canvas.create_text(500, y+10, text='HURÁ', fill='green', font='Arial 15')
    else:
        canvas.create_text(500, y+10, text='ŠKODA', fill='red', font='Arial 15')

   
    y += 30
    

canvas.mainloop()