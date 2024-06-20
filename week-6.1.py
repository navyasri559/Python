from tkinter import *
def draw_rectangle(canvas, coordinates, color):
    canvas.pack(pady=20)
    canvas.create_rectangle(rectangle,color)
window = Tk()
window.title("Canvas")
window.geometry("500x500")
mycan = Canvas(window, width=300, height=250, bg="magenta")
mycan.pack(pady=20)
x = (50, 50, 250, 200)
color = "pink"
draw_rectangle(mycan, x, color)
window.mainloop()