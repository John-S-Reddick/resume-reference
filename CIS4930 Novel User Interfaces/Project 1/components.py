import tkinter
from tkinter import *
import numpy as np
import tkinter as tk
import main as m
from os.path import exists
from tempfile import TemporaryFile
import recognizers as r
import data as d

# Numbers involved in Entry creation
X = m.X
Y = m.Y
STROKE = m.STROKE
DIMENSIONS = m.DIMENSIONS
IGNORE = -m.IGNORE
FIRST = m.FIRST

WIDTH = m.WIDTH
HEIGHT = m.HEIGHT

CANV_WIDTH = m.CANV_WIDTH
CANV_HEIGHT = m.CANV_HEIGHT

CANV_SIDE = m.CANV_SIDE

# Symbols as required by Dr. Pittman
SYMBOLS = m.SYMBOLS
DIRECTORY = m.DIRECTORY
NAME = m.NAME
EXTENSION = m.EXTENSION
SAMPLES = m.SAMPLES

RESAMPLE_N = m.RESAMPLE_N


class DrawingArea2:
    def __init__(self, director):
        self.director = director
        self.data = director.data
        self.s = director.settings
        self.dra = (0, 0, 0, 0)

        self.canvas = tk.Canvas(
            self.director.frame,
            width=self.s['width'],
            height=self.s['height'],
            bg=self.s['bg'])

    def clear_canvas(self):
        self.canvas.create_rectangle(
            (0, 0),
            (self.s['width'],
             self.s['height']),
            fill=self.s['bg'])

    def load_sketch(self, connect_dots=True):
        self.sketch(self.data.points, connect_dots)

    def sketch(self, points, connect_dots=True):
        self.clear_canvas()
        p1 = points[FIRST]
        if connect_dots:
            for p2 in points:
                if p1[STROKE] == p2[STROKE]:
                    self.canvas.create_rectangle(
                        p1[X], p1[Y],
                        p2[X], p2[Y]
                    )
                p1 = p2
        else:
            for p in points:
                self.canvas.create_rectangle(
                    p[X] - self.s['point_width'],
                    p[Y] - self.s['point_width'],
                    p[X], p[Y]
                )

    def draw_text(self):
        self.canvas.create_text(
            (200, 200),
            text=self.director.text,
            font=self.s['font']
        )

    def paint(self):
        l = self.data.points.shape[0] - 1
        if l > 0:
            p1 = self.data.points[l - 1]
            p2 = self.data.points[l]
            if p1[STROKE] == p2[STROKE]:
                self.canvas.create_rectangle(
                    p1[X], p1[Y],
                    p2[X], p2[Y]
                )


class Binds:
    def __init__(self, director, element, mode):
        canvas = element.canvas
        frame = director.frame
        canvas.bind("<Button-1>", director.mouse_down)
        canvas.bind("<Button-2>", director.undo)
        canvas.bind("<B1-Motion>", director.paint)
        canvas.bind_all("<Control-Key-z>", director.undo)
        canvas.bind_all("<Control-Key-y>", director.redo)
        canvas.bind_all("<Control-Key-x>", director.erase_sketch)
        canvas.bind_all("<ButtonRelease-1>", director.mouse_up)

        undo_button = Button(director.frame, text="Undo", command=director.undo)
        redo_button = Button(director.frame, text="Redo", command=director.redo)
        erase_button = Button(director.frame, text="Clear Canvas", command=director.erase_sketch)

        if mode == "Training":
            canvas.bind("<Button-3>", director.write_template)
            # self.element.bind("<Return>", director.write_template)
            submit_button = Button(
                director.frame,
                text="Submit Template",
                command=director.write_template)

        if mode == "Evaluation":
            canvas.bind("<Button-3>", director.recognize)
            # self.element.bind("<Return>", director.resample)
            # self.element.bind("<Return>", director.recognize)
            submit_button = Button(
                director.frame,
                text="Recognize",
                command=director.recognize)


class Welcome:
    def __init__(self, master):
        master.geometry('300x200')
        master.resizable(False, False)
        self.app = None
        self.newWindow = None
        self.master = master
        self.frame = tk.Frame(self.master)
        pre_trained = tk.Button(
            master,
            text='Enter Pre-trained drawing area',
            command=self.pre_trained
        )
        self.frame = tk.Frame(self.master)
        trained_button = tk.Button(
            master,
            text='Enter Training',
            command=self.to_train
        )
        pre_trained.pack()
        trained_button.pack()
        self.frame.pack()

    def pre_trained(self):
        self.newWindow = tk.Toplevel(self.master)

        self.app = SketchWindow(self.newWindow, option='recognition')

    def to_train(self):
        self.newWindow = tk.Toplevel(self.master)

        self.app = SketchWindow(self.newWindow, option='training')


class SketchWindow:
    def __init__(self, master, option='recognition'):
        self.app = None
        self.newWindow = None
        self.master = master

        self.frame = tk.Frame(self.master)
        self.director = d.Director(self.frame)

        if option == 'recognition':
            self.director.enter_recogntion()

        if option == 'training':
            self.director.enter_training()

        self.frame.pack()
