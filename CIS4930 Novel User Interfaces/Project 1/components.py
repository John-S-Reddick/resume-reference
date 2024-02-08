from tkinter import *
import numpy as np
import tkinter as tk
from os.path import exists
from tempfile import TemporaryFile
import recognizers as r

WINDOW_SCALER = .5
CANVAS_SCALER = 1
GAP_SCALER = 1 - CANVAS_SCALER / 4

# Numbers involved in Entry creation
X = 0
Y = 1
STROKE = 2
DIMENSIONS = 3
IGNORE = -1

WIDTH = 1920
HEIGHT = 1080

CANV_WIDTH = WIDTH * WINDOW_SCALER
CANV_HEIGHT = HEIGHT * WINDOW_SCALER

CANV_SIDE = CANV_WIDTH

# Symbols as required by Dr. Pittman
SYMBOLS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', 't', 'a', 'n', 's', 'c', 'i']
SAVEZ = 'templates'
TEMPLATES = 'templates.npz'
SAMPLES = 5


class DrawingArea:
    def __init__(self, master, nphandler):
        self.master = master
        self.np_handler = nphandler
        self.points = np.array([[-1, -1, -1]])
        self.undo_stack = []
        self.redo_stack = []
        self.x1 = IGNORE
        self.y1 = IGNORE
        self.stroke_count = -1
        self.canvas = tk.Canvas(master, width=CANV_SIDE, height=CANV_SIDE, bg='white')
        self.binds()
        self.canvas.pack
        self.buttons = DrawingButtons(master=self.master, canvas=self)
        self.draw_prompt()
    ###
        """ Drawing """
    ###
    def draw_prompt(self):
        s = str(self.np_handler.current_symbol())
        self.canvas.create_text(
            (300, 100),
            text="Please draw: " + s,
            font='tkDefaeultFont 24')
    def painting(self, x2, y2):
        if self.x1 == -1 or self.y1 == -1:
            self.x1 = x2
            self.y1 = y2
        self.canvas.create_line(self.x1, self.y1, x2, y2)
        self.x1 = x2
        self.y1 = y2
    def load_sketch(self, sketch):
        self.clear_canvas()
        line1 = -1

        for line2 in sketch:
            if line1 != line2[STROKE]:
                self.x1 = -1
                self.y1 = -1
            self.painting(line2[X], line2[Y])
            line1 = line2[STROKE]
    def drag_handler(self, event):
        self.painting(event.x, event.y)
        newpoint = np.array([[event.x, event.y, self.stroke_count]])
        self.points = np.concatenate((self.points, newpoint), axis=0)
    def erase_sketch(self, *event):
        self.points = np.array([[-1, -1, -1]])
        self.undo_stack.append(self.points)
        self.stroke_count = -1
        self.clear_canvas()

    def clear_canvas(self):
        self.x1 = -1
        self.y1 = -1
        self.canvas.create_rectangle((0, 0), (CANV_SIDE, CANV_SIDE), fill='white')
        self.draw_prompt()
        ###
        """ Data Management """

    ###
    def undo(self, *event):
        if self.undo_stack:
            self.redo_stack.append(self.points)
            self.points = self.undo_stack.pop()
            self.stroke_count = self.stroke_count - 1

        else:
            self.clear_canvas()

        self.load_sketch(self.points)

    def redo(self, *event):
        if self.redo_stack:
            self.undo_stack.append(self.points)
            self.points = self.redo_stack.pop()
            self.stroke_count = self.stroke_count + 1

        self.load_sketch(self.points)

    def submit(self, *event):
        # trigger training
        if self.np_handler.training:
            self.np_handler.increment(self.points)
            self.erase_sketch()
        # Trigger recognition
        else:
            pass
            
        """ User Interaction """
    ##
    def mouse_up(self, event):
        self.redo_stack.append(self.points)

    def mouse_click(self, event):
        self.stroke_count += 1
        self.x1 = -1
        self.y1 = -1
        self.undo_stack.append(self.points)
        print(self.points)

    def binds(self):
        # Key Binding tutorial
        # https://www.tutorialexample.com/python-tkinter-bind-ctrlkey-python-tutorial/
        # https://dafarry.github.io/tkinterbook/tkinter-events-and-bindings.htm
        self.canvas.bind("<Button-1>", self.mouse_click)
        self.canvas.bind("<B1-Motion>", self.drag_handler)
        self.canvas.bind_all("<Control-Key-z>", self.undo)
        self.canvas.bind_all("<Control-Key-y>", self.redo)
        self.canvas.bind_all("<Control-Key-x>", self.erase_sketch)
        self.canvas.bind_all("<Return>", self.submit)
        self.canvas.pack()
        # self.bind("<ButtonRelease-1>", mouse_up)

        # subButton = Button(root, text="Submit", command=save)
        # subButton.grid(column=0, row=1)


class DrawingButtons:
    def __init__(self, master, canvas):

        if not canvas.np_handler.training:
            subtext = 'Recognize Sketch'
        else:
            subtext = 'Save template'

        prompt = Label(master, text=canvas.np_handler.current_symbol())
        undo_button = Button(master, text="Undo", command=canvas.undo)
        redo_button = Button(master, text="Redo", command=canvas.redo)
        erase_button = Button(master, text="Clear Canvas", command=canvas.erase_sketch)
        submit_button = Button(master, text=subtext, command=canvas.submit)

        prompt.pack()
        undo_button.pack()
        redo_button.pack()
        erase_button.pack()
        submit_button.pack()


# Proceed through 5 drawings of symbols, displaying and submitting each
# Once complete, close training window and open testing window

class Training:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.canvas = DrawingArea(master=self.frame, nphandler=TrainingHandler())
        self.frame.pack()

        def new_window():
            self.newWindow = tk.Toplevel(self.master)
            self.app = evaluation(self.newWindow)


class TrainingHandler:
    def __init__(self, symbols=SYMBOLS, samples=SAMPLES):
        if not exists(TEMPLATES):
            self.key = np.zeros(len(symbols) + 1)
            np.savez(SAVEZ, key=self.key)
        self.templates = np.load(TEMPLATES)
        self.training = True
        self.key = self.templates['key']
        self.generation = int(self.key[0])
        self.symbols = symbols
        self.samples = samples
        self.inc = 0
        self.entry_names = []
        for s in symbols:
            self.entry_names.append('tmplt' + str(self.generation) + s)
    # Keywords numpy savez
    # https://stackoverflow.com/questions/33878179/use-value-of-variable-rather-than-keyword-in-python-numpy-savez
    def ind(self):
        return int(self.inc / self.samples)
    def current_symbol(self):
        return self.symbols[self.ind()]
    def increment(self, points):
        index = self.ind()
        current_entry = self.entry_names[index]
        np.savez(SAVEZ, **{current_entry: points})
        print ("Saved to: " + current_entry)
        self.inc += 1
        if self.inc >= len(self.symbols) * self.samples:
            self.key[FIRST] = self.generation + 1
            np.savez(SAVEZ, key=self.key)
            self.training = False







class evaluation:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text='Quit', width=25, command=self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()
