import tkinter

n = int(input('n: '))

length = 200/n

x0 = 100
y0 = 100
x1 = 500
y1 = 500

canvas = tkinter.Canvas(width=600, height=600)
canvas.pack()

for i in range(n):
    if i%3 == 0:
        color = 'red'
    elif i%3 == 1:
        color = 'blue'
    elif i%3 == 2:
        color = 'yellow'


    canvas.create_rectangle(x0,y0,x1,y1, fill=color)

    x0 += length
    y0 += length
    x1 -= length
    y1 -= length

canvas.mainloop()