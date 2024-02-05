from tkinter import *
import numpy as np

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

#Numbers involved in Entry creation
ENTRY_X = 0
ENTRY_Y = 1
ENTRY_STROKE = 2
DIMENSIONS = 3

FILE_NAME = "data_out.csv"


WIDTH = 1920
HEIGHT = 1080

width = WIDTH * WINDOW_SCALER
height = HEIGHT * WINDOW_SCALER

# Create array of Zeros NumPy
# https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros
coordinateList = []
prvList = []

currentStroke = -1
last_x = -1
last_y = -1


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
    print(coordinateList)

def painting(x, y):
    global last_x
    global last_y
    if last_x == -1 or last_y == -1:
        last_x = x
        last_y = y
    canvas1.create_line(last_x, last_y, x, y)

    last_x = x
    last_y = y

def load_sketch(list):
    global last_x
    global last_y

    clear_canvas()
    last_stroke = -1



    for i in list:
        if last_stroke != i[2]:
            last_x = -1
            last_y = -1
        painting(i[ENTRY_X], i[ENTRY_Y])
        last_stroke = i[ENTRY_STROKE]

def drag_handler(event):
    global currentStroke

    painting(event.x, event.y)
    coordinateList.append(np.array([event.x, event.y, currentStroke]))

def clear_canvas():
    global last_x
    global last_y
    last_x = -1
    last_y = -1
    canvas1.create_rectangle((0,0), (canvasSize, canvasSize), fill='white')

# Optional arguments in python function calls
# https://stackoverflow.com/questions/9539921/how-do-i-define-a-function-with-optional-arguments

def undo(*event):
    global currentStroke
    global coordinateList
    global prvList
    newList = []
    prvList = coordinateList

    for entry in coordinateList:
        if entry[2] < currentStroke:
            newList.append(entry)
        else:
            break

    currentStroke = currentStroke - 1
    coordinateList = newList
    load_sketch(coordinateList)

def redo(*event):
    global currentStroke
    global coordinateList
    global prvList

    coordinateList = prvList
    currentStroke = currentStroke + 1
    load_sketch(coordinateList)

def erase_canvas(*event):
    global currentStroke
    global coordinateList
    global prvList

    prvList = coordinateList
    coordinateList = []

    clear_canvas()
def save(*event):
    sizeOfDataArray = len(coordinateList)

    #How Numpy Zeros work: https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros
    arr = np.zeros((sizeOfDataArray, DIMENSIONS), dtype='int')
    index = 0
    for entry in coordinateList:
        arr[index] = entry
        index += 1

    #From https: // numpy.org / doc / stable / reference / generated / numpy.save.html  # numpy.save
    with open(OUTPUT_FILE_NAME, 'wb') as f:
        np.save(f, arr)




def submit():
    print("bupsmit")


root = tk.Tk()
root.geometry('1920x1080')
root.title('Canvas Demo')

# Key Binding tutorial
# https://www.tutorialexample.com/python-tkinter-bind-ctrlkey-python-tutorial/
root.bind_all("<Control-Key-z>", undo)
root.bind_all("<Control-Key-y>", redo)
root.bind_all("<Control-Key-x>", erase_canvas)
root.bind_all("<Return>", save)

canvas1 = tk.Canvas(root, width=canvasSize, height=canvasSize, bg='white')

canvas1.grid(column=0,row=0)

# https://dafarry.github.io/tkinterbook/tkinter-events-and-bindings.htm
canvas1.bind("<Button-1>", mouse_click)
canvas1.bind("<B1-Motion>", drag_handler)



canvas2 = tk.Canvas(root, width=canvasSize, height=canvasSize, bg='white')
canvas2.grid(column=1,row=0)

subButton = Button(root, text="Submit", command=save)
subButton.grid(column=0,row=1)

undoButton = Button(root, text="Undo", command=undo)
undoButton.grid(column=1,row=1)

redoButton = Button(root, text="Redo", command=redo)
redoButton.grid(column=2,row=1)

eraseButton = Button(root, text="Clear Canvas", command=erase_canvas)
eraseButton.grid(column=3,row=1)

root.mainloop()