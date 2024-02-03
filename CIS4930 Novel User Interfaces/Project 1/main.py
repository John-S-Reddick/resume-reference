from tkinter import *
import numpy as np

# Windows for Tkinter
# https://likegeeks.com/python-gui-examples-tkinter-tutorial/

# Tkinter canvases
# https://www.pythontutorial.net/tkinter/tkinter-canvas/

# Tkinter window and Grid management:
# https://www.pythonguis.com/tutorials/use-tkinter-to-design-gui-layout/

# Tkinter events ranked by subjective usefulness
# 1. https://stackoverflow.com/questions/32289175/list-of-all-tkinter-events
# 2. https://www.tutorialexample.com/python-tkinter-bind-ctrlkey-python-tutorial/
# 3. https://dafarry.github.io/tkinterbook/tkinter-events-and-bindings.htm
# 4. https://tkinterexamples.com/events/mouse/

# Tkinter components ranked by subjective usefulness
# 1. https://www.geeksforgeeks.org/tkinter-cheat-sheet/


# Writing to a file
# https://www.geeksforgeeks.org/writing-to-file-in-python/



# PyInstaller
# https://pyinstaller.org/en/stable/



# Print Options
# https://numpy.org/doc/stable/reference/generated/numpy.set_printoptions.html
np.set_printoptions()

WINDOW_SCALER = .5
CANVAS_SCALER = 1
GAP_SCALER = 1 - CANVAS_SCALER / 4

FILE_NAME = "data_out.csv"


WIDTH = 1920
HEIGHT = 1080

width = WIDTH * WINDOW_SCALER
height = HEIGHT * WINDOW_SCALER

# Create array of Zeros NumPy
# https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros
list = []

currentStroke = -1
last_x = -1
last_y = -1

file1 = open(FILE_NAME, "w")

canvasSize = width * CANVAS_SCALER

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)



import tkinter as tk

#Refer to mouse events for more information


#Increases current stroke count
def mouse_click(event):
    global currentStroke
    global last_x
    global last_y

    currentStroke = currentStroke + 1
    last_x = -1
    last_y = -1
    print(list)

def drag_handler(event):
    global currentStroke
    global last_x
    global last_y
    if last_x == -1 or last_y == -1:
        last_x = event.x
        last_y = event.y
    canvas1.create_line(last_x, last_y, event.x, event.y)
    list.append(np.array([event.x, event.y, currentStroke]))
    last_x = event.x
    last_y = event.y

def drag_handler(event):
    global currentStroke
    global last_x
    global last_y
    if last_x == -1 or last_y == -1:
        last_x = event.x
        last_y = event.y

    canvas1.create_line(last_x, last_y, event.x, event.y)
    list.append(np.array([event.x, event.y, currentStroke]))
    last_x = event.x
    last_y = event.y

def undo(event):
    print("bazinga")

def redo(event):
    print("agnizab")

def submit():
    print("bupsmit")


root = tk.Tk()
root.geometry('1920x1080')
root.title('Canvas Demo')

# Key Binding tutorial
# https://www.tutorialexample.com/python-tkinter-bind-ctrlkey-python-tutorial/
root.bind_all("<Control-Key-z>", undo)
root.bind_all("<Control-Key-y>", redo)
root.bind_all("<Return>", redo)

canvas1 = tk.Canvas(root, width=canvasSize, height=canvasSize, bg='white')

canvas1.grid(column=0,row=0)

# https://dafarry.github.io/tkinterbook/tkinter-events-and-bindings.htm
canvas1.bind("<Button-1>", mouse_click)
canvas1.bind("<B1-Motion>", drag_handler)



canvas2 = tk.Canvas(root, width=canvasSize, height=canvasSize, bg='white')
canvas2.grid(column=1,row=0)

subButton = Button(root, text="Submit", command=submit)
subButton.grid(column=0,row=1)
root.mainloop()