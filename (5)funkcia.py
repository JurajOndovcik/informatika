import tkinter

y = -1
a = int(input('a: '))
x = 2
b = int(input('b: '))

y2 = a*x+b
if y2 == y:
    print('Leží')
else:
    print('Neleží')

Px = [(0-b)/a,0]
Py = [0, b]
print(Px, Py)

canvas = tkinter.Canvas(width=600, height=600)
canvas.pack()

canvas.create_line(100,300,500,300)
canvas.create_line(300,100,300,500)
canvas.create_oval(300+(x*20), 300-(y*20), 300+(x*20)+10, 300-(y*20)+10)


canvas.create_line(300+(Px[0]*20), 300+(Py[0]*20), 300-(Px[1]*20), 300-(Py[1]*20))

canvas.mainloop()