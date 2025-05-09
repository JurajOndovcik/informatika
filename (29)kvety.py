import random
import tkinter

canvas = tkinter.Canvas(width=800, height=600, bg="white")
canvas.pack()
canvas.create_rectangle(0, 0, 400, 300, fill="red")
canvas.create_rectangle(400, 0, 800, 300, fill="green")
canvas.create_rectangle(0, 300, 400, 600, fill="blue")
canvas.create_rectangle(400, 300, 800, 600, fill="yellow")

red = 0
green = 0
blue = 0
yellow = 0
color = "black"

for i in range(100,500):
    x = random.randint(0, 800)
    y = random.randint(0, 600)
    if 0 <= x < 400 and 0 <= y < 300:
        red += 1
        color = "red"
    elif 400 <= x < 800 and 0 <= y < 300:
        green += 1
        color = "green"
    elif 0 <= x < 400 and 300 <= y < 600:
        blue += 1
        color = "blue"
    elif 400 <= x < 800 and 300 <= y < 600:
        yellow += 1
        color = "yellow"
    canvas.create_oval(x-2.5, y-2.5, x+2.5, y+2.5, fill=color, outline="black")

# Determine the most used color
counts = {"red": red, "green": green, "blue": blue, "yellow": yellow}
most_used_color = max(counts, key=counts.get)

print("Red: ", red)
print("Green: ", green)
print("Blue: ", blue)
print("Yellow: ", yellow)
print(f"Most used color: {most_used_color}")
canvas.mainloop()