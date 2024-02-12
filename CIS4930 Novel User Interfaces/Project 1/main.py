from tkinter import *
import tkinter as tk
import numpy as np
import components as comps


WINDOW_SCALER = .5
CANVAS_SCALER = 1
GAP_SCALER = 1 - CANVAS_SCALER / 4

# Numbers involved in Entry creation
X = 0
Y = 1
STROKE = 2
DIMENSIONS = 3
IGNORE = -1
FIRST = 0
SECOND = 1

RESAMPLE_N = 64

WIDTH = 1920
HEIGHT = 1080

CANV_WIDTH = WIDTH * WINDOW_SCALER
CANV_HEIGHT = HEIGHT * WINDOW_SCALER

CANV_SIDE = CANV_WIDTH

# Symbols as required by Dr. Pittman
SYMBOLS = [
    '0', '1', '2',
    '3', '4', '5', '6',
    '7', '8', '9', '+',
    '-', '.', 't', 'a',
    'n', 's', 'c', 'i'
]
DIRECTORY = 'templates/'
NAME = 'tmplt.'
EXTENSION = '.npy'
SAMPLES = 5
BBOX_SIZE = 200

#
np.set_printoptions()



def main():
    root = tk.Tk()
    app = comps.Welcome(root)
    root.mainloop()

# def main():
#print(r.OneDollar.resample())

if __name__ == '__main__':
    main()
