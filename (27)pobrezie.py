import tkinter
lampy = 1

canvas = tkinter.Canvas(width=1000, height=650, bg="white")
canvas.pack()
canvas.create_rectangle(0, 0, 1000, 325, fill="green")
canvas.create_rectangle(0, 325, 1000, 650, fill="blue")
canvas.create_line(0, 325, 1000, 325, fill="black", width=4)

def lampa(pozicia):
    global lampy

    x = pozicia.x
    y = pozicia.y

    if y < 325:
        if lampy >= 10:
            print('Je tam veľa lamp')
        else:
            canvas.create_rectangle(x-5, y, x+5, y+50, fill="grey")
            canvas.create_oval(x-10, y-10, x+10, y+10, fill="yellow")
            canvas.create_rectangle(x-10, y+30, x+10, y+70, fill="gray", outline="black")
            canvas.create_text(x, y+50, text=lampy, font="Arial 15", fill="black")

            otocena_lampa(x, y)
            lampy += 1
    else:
        print('Nedá sa')
def otocena_lampa(x, y):
    global lampy

    canvas.create_rectangle(x-5, 650-y, x+5, 650-y-50, fill="grey")
    canvas.create_oval(x-10, 650-y-10, x+10, 650-y+10, fill="yellow")
    canvas.create_rectangle(x-10, 650-y-30, x+10, 650-y-70, fill="gray", outline="black")
    canvas.create_text(x, 650-y-50, text=lampy, font="Arial 15", fill="black", angle=180)
    

canvas.bind("<Button-1>", lampa)
canvas.mainloop()