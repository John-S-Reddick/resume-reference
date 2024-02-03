from tkinter import *

# Windows for Tkinter
# https://likegeeks.com/python-gui-examples-tkinter-tutorial/

# Canvas
# https://www.pythontutorial.net/tkinter/tkinter-canvas/

# Mouse Events (In order of helpfulness)
# 1. https://stackoverflow.com/questions/32289175/list-of-all-tkinter-events
# 2. https://dafarry.github.io/tkinterbook/tkinter-events-and-bindings.htm
# 3. https://tkinterexamples.com/events/mouse/

# List of all tkinter events
# https://stackoverflow.com/questions/32289175/list-of-all-tkinter-events

# Writing to a file
# https://www.geeksforgeeks.org/writing-to-file-in-python/

# PyInstaller
# https://pyinstaller.org/en/stable/

WINDOW_SCALER = .5
CANVAS_SCALER = 1
GAP_SCALER = 1 - CANVAS_SCALER / 4

FILE_NAME = "data_out.csv"


WIDTH = 1920
HEIGHT = 1080

width = WIDTH * WINDOW_SCALER
height = HEIGHT * WINDOW_SCALER

currentX = 0
currentY = 0
file1 = open(FILE_NAME, "w")

canvasSize = width * CANVAS_SCALER

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)



import tkinter as tk

#Refer to mouse events for more information



def drag_handler(event):
    print(event.x, event.y)


root = tk.Tk()
root.geometry('1920x1080')
root.title('Canvas Demo')

canvas1 = tk.Canvas(root, width=canvasSize, height=canvasSize, bg='white')

canvas1.grid(column=0,row=0)

# https://dafarry.github.io/tkinterbook/tkinter-events-and-bindings.htm
canvas1.bind("<Button-1>", lambda x: print("LEFT CLICK"))
canvas1.bind("<B1-Motion>", drag_handler)
canvas1.bind("<ButtonRelease-1>", print("waxum"))

canvas2 = tk.Canvas(root, width=canvasSize, height=canvasSize, bg='white')
canvas2.grid(column=1,row=0)

root.mainloop()