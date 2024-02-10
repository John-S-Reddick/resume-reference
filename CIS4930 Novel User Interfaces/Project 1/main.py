from tkinter import *
import tkinter as tk
import numpy as np
import recognizers as r
import components as comps


#

#
np.set_printoptions()



def main():
    root = tk.Tk()
    app = comps.Welcome(root)
    root.mainloop()

if __name__ == '__main__':
    main()
