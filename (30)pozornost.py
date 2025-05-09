import tkinter
import random

canvas = tkinter.Canvas(width=500, height=500, bg='white')
canvas.pack()

r = 30
score = 0
score_display = canvas.create_text(50, 20, text=f"Score: {score}", font=("Arial", 16))
circle = None
rounds_played = 0
total_rounds = 10

def show_circle():
    global circle
    x = random.randint(r, 500 - r)
    y = random.randint(r, 500 - r)
    if circle:
        canvas.delete(circle)
    circle = canvas.create_oval(x - r, y - r, x + r, y + r, fill="red", tags="target")
    canvas.after(1000, next_round)

def next_round():
    global rounds_played
    rounds_played += 1
    if rounds_played < total_rounds:
        show_circle()
    else:
        game_over()

def handle_click(event):
    global score
    if circle:
        items_clicked = canvas.find_overlapping(event.x, event.y, event.x, event.y)
        if canvas.find_withtag("target")[0] in items_clicked:
            score += 10
        else:
            score -= 1
        canvas.itemconfig(score_display, text=f"Score: {score}")

def game_over():
    if circle:
        canvas.delete(circle)
    canvas.unbind("<Button-1>")
    canvas.create_text(250, 250, text=f"Game Over! Final Score: {score}", font=("Arial", 20))

canvas.bind("<Button-1>", handle_click)
show_circle()
canvas.mainloop()