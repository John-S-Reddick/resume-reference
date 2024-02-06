from tkinter import *

import numpy
import numpy as np
import recognizers as r

# Optional arguments in python function calls
# https://stackoverflow.com/questions/9539921/how-do-i-define-a-function-with-optional-arguments

# Windows for Tkinter
# https://likegeeks.com/python-gui-examples-tkinter-tutorial/

# Tkinter canvases
# https://www.pythontutorial.net/tkinter/tkinter-canvas/

# Tkinter window and Grid management:
# https://www.pythonguis.com/tutorials/use-tkinter-to-design-gui-layout/

# Tkinter events ranked by subjective usefulness/relevance
# 1. https://stackoverflow.com/questions/32289175/list-of-all-tkinter-events
# 2. https://www.tutorialexample.com/python-tkinter-bind-ctrlkey-python-tutorial/
# 3. https://dafarry.github.io/tkinterbook/tkinter-events-and-bindings.htm
# 4. https://tkinterexamples.com/events/mouse/

# Tkinter components ranked by subjective usefulness
# 1. https://www.geeksforgeeks.org/tkinter-cheat-sheet/

# Saving and loading with Numpy
# https://numpy.org/doc/stable/reference/generated/numpy.save.html#numpy.save
# https://numpy.org/doc/stable/reference/generated/numpy.load.html#numpy.load


# PyInstaller
# https://pyinstaller.org/en/stable/


# Print Options
# https://numpy.org/doc/stable/reference/generated/numpy.set_printoptions.html
np.set_printoptions()

WINDOW_SCALER = .5
CANVAS_SCALER = 1
GAP_SCALER = 1 - CANVAS_SCALER / 4

OUTPUT_FILE_NAME = 'test.npy'

# Numbers involved in Entry creation
X = 0
Y = 1
STROKE = 2
DIMENSIONS = 3
IGNORE = -1
FILE_NAME = "data_out.csv"

WIDTH = 1920
HEIGHT = 1080

width = WIDTH * WINDOW_SCALER
height = HEIGHT * WINDOW_SCALER

# Create array of Zeros NumPy
# https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros
points = np.array([[-1, -1, -1]])
undo_stack = []
redo_stack = []

stroke_count = -1
x1 = IGNORE
y1 = IGNORE

canvasSize = width * CANVAS_SCALER


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)


import tkinter as tk


# Refer to mouse events for more information


# Increases current stroke count
def mouse_up(event):
    redo_stack.append(points)


def mouse_click(event):
    global stroke_count
    global x1
    global y1

    stroke_count += 1
    x1 = -1
    y1 = -1

    undo_stack.append(points)

    print(points)


def painting(x2, y2):
    global x1
    global y1
    if x1 == -1 or y1 == -1:
        x1 = x2
        y1 = y2
    canvas1.create_line(x1, y1, x2, y2)

    x1 = x2
    y1 = y2


def load_sketch(sketch):
    global x1
    global y1

    clear_canvas()
    line1 = -1

    for line2 in sketch:
        if line1 != line2[STROKE]:
            x1 = -1
            y1 = -1
        painting(line2[X], line2[Y])
        line1 = line2[STROKE]


def drag_handler(event):
    global points
    global stroke_count

    painting(event.x, event.y)
    newpoint = np.array([[event.x, event.y, stroke_count]])
    points = np.concatenate((points, newpoint), axis=0)


def clear_canvas():
    global x1
    global y1
    x1 = -1
    y1 = -1
    canvas1.create_rectangle((0, 0), (canvasSize, canvasSize), fill='white')


# Optional arguments in python function calls
# https://stackoverflow.com/questions/9539921/how-do-i-define-a-function-with-optional-arguments

def undo(*event):
    global stroke_count
    global points
    global undo_stack
    global redo_stack
    if undo_stack:
        redo_stack.append(points)
        points = undo_stack.pop()
        stroke_count = stroke_count - 1

    else:
        clear_canvas()

    load_sketch(points)


def redo(*event):
    global stroke_count
    global points
    global undo_stack
    global redo_stack
    if redo_stack:
        undo_stack.append(points)
        points = redo_stack.pop()
        stroke_count = stroke_count + 1

    load_sketch(points)


def erase_canvas(*event):
    global stroke_count
    global points
    global back_up_points

    points = np.array([[-1, -1, -1]])
    undo_stack.append(points)

    clear_canvas()


def save(*event):
    # From https: // numpy.org / doc / stable / reference / generated / numpy.save.html  # numpy.save
    with open(OUTPUT_FILE_NAME, 'wb') as f:
        np.save(f, points)


root = tk.Tk()
root.geometry('1920x1080')
root.title('Canvas Demo')

# Key Binding tutorial
# https://www.tutorialexample.com/python-tkinter-bind-ctrlkey-python-tutorial/
root.bind_all("<Control-Key-z>", undo)
root.bind_all("<Control-Key-y>", redo)
root.bind_all("<Control-Key-x>", erase_canvas)
# root.bind_all("<ButtonRelease-1>", mouse_up)
root.bind_all("<Return>", save)

canvas1 = tk.Canvas(root, width=canvasSize, height=canvasSize, bg='white')

canvas1.grid(column=0, row=0)

# https://dafarry.github.io/tkinterbook/tkinter-events-and-bindings.htm
canvas1.bind("<Button-1>", mouse_click)
canvas1.bind("<B1-Motion>", drag_handler)

canvas2 = tk.Canvas(root, width=canvasSize, height=canvasSize, bg='white')
canvas2.grid(column=1, row=0)

subButton = Button(root, text="Submit", command=save)
subButton.grid(column=0, row=1)

undoButton = Button(root, text="Undo", command=undo)
undoButton.grid(column=1, row=1)

redoButton = Button(root, text="Redo", command=redo)
redoButton.grid(column=2, row=1)

eraseButton = Button(root, text="Clear Canvas", command=erase_canvas)
eraseButton.grid(column=3, row=1)

root.mainloop()
