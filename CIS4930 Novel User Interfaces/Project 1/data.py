import numpy as np
import components as c
import main as m
import recognizers as r
from os.path import exists

from recognizers import OneDollar

# WINDOW_SCALER = .5
CANVAS_SCALER = m.CANVAS_SCALER
GAP_SCALER = m.GAP_SCALER

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

BBOX_SIZE = m.BBOX_SIZE


class Director:
    def __init__(self, master):
        self.frame = master
        self.binds = None
        self.settings = {
            'width': CANV_WIDTH,
            'height': CANV_HEIGHT,
            'point_width': 2,
            'bg': 'white',
            'font': 'tkDefaeultFont 24'
        }
        self.text = ""
        self.data = Data2()
        self.templater = TemplateManger(self)
        self.canvas = c.DrawingArea2(self)
        self.display = c.DrawingArea2(self)
        self.display.canvas.pack()
        self.canvas.canvas.pack()

        self.canvas.load_sketch(False)

    def enter_training(self):
        self.binds = c.Binds(director=self, element=self.canvas, mode="Training")
        self.training_text(self.templater.get_status())

    def enter_recogntion(self):
        self.binds = c.Binds(director=self, element=self.canvas, mode="Evaluation")

    def recognize(self, *event):
        t = self.templater
        one_d = t.recog_one_dollar()
        status = t.status(one_d[0])
        self.recognition_text(status)


    def recognition_text(self, status):
        status = status
        self.text = \
            "One Dollar: " + status["symbol"] + '\nAcc:'\
            "--- " + status["symbol"] + '\n'
        self.update_text(self.display)

    def training_text(self, status):
        status = status
        self.text = \
            "Current Symbol: " + status["symbol"] + '\n' + \
            status['symbol'] + 's: ' + str(status['subdex']) + '/' + str(SAMPLES) + \
            '\nSymbol: ' + str(status['symdex']) + '/' + str(len(SYMBOLS) - 2) + \
            '\nTotal progress: ' + str(status['index']) + '/' + str(status['total']) + \
            "\n\nCurrent Symbol: " + status["symbol"] + \
            '\nNext Symbol: ' + str(status['next_symbol']) + \
            '\nPrevious Symbol ' + str(status['prv_symbol'])
        self.update_text(self.display)

    def write_template(self, *events):
        status = self.templater.train(self.data.points)
        self.training_text(status)
        self.data.initialize_points()
        # Clear
        return status['done']

    def update_text(self, element):
        element.clear_canvas()
        element.draw_text()

    def redo(self, *event):
        self.data.redo()
        self.canvas.load_sketch(True)
        self.canvas.draw_text()

    def undo(self, *event):
        self.data.undo()
        self.canvas.load_sketch(True)
        self.canvas.draw_text()

    def paint(self, event):
        self.data.add_point(event)
        self.canvas.paint()

    def erase_sketch(self):
        self.canvas.clear_canvas()

    def mouse_down(self, event):
        self.data.click()

    def mouse_up(self, event):
        self.data.mouse_up()


class TemplateManger:
    def __init__(self, director):
        self.director = director
        self.data = director.data
        self.save_list = []
        for s in SYMBOLS:
            for i in range(SAMPLES):
                self.save_list.append(DIRECTORY + NAME + s + '.' + str(i))

        self.load_list = []
        self.templates = []
        for entry in self.save_list:
            entry = entry + EXTENSION
            self.load_list.append(entry)
            if exists(entry):
                self.templates.append(np.load(entry))

        self.training = 0

        self.one_dollar = r.OneDollar(self.templates)

    def create_template(self, path):
        np.save(path, self.data.points)
        self.data.reset()

    def get_status(self):
        return self.status(int(self.training))

    def status(self, ind):
        sub_template_index = int(self.training % SAMPLES)
        symbol_index = int(self.training / SAMPLES)
        template = None
        path = self.load_list[ind]
        if symbol_index + 1 >= len(SYMBOLS):
            next_symbol = 'Done!'
        else:
            next_symbol = SYMBOLS[symbol_index + 1]
        if exists(path):
            template = np.load(path)
        return ({
            "index": ind,
            "load": path,
            "save": self.save_list[ind],
            "load_tmplt": template,
            "subdex": sub_template_index,
            "symdex": symbol_index,
            "symbol": SYMBOLS[symbol_index],
            "total": (len(SYMBOLS)) * SAMPLES,
            "next_symbol": next_symbol,
            "prv_symbol": SYMBOLS[symbol_index - 1],
            "done": ind >= len(SYMBOLS) - 1
        })

    def train(self):
        status = self.get_status()
        self.create_template(status['save'])
        self.training += 1
        return status

    def recog_one_dollar(self):
        return self.one_dollar.sketch(self.data.points)


class Data2:
    def __init__(self):
        self.points = np.array([[-1, -1, -1]])
        self.stroke_count = -1
        self.undo_stack = []
        self.redo_stack = []
        self.inc = 0
        self.last_inc = 0
        self.next_inc = 0

        self.text = ""

    def add_point(self, event):
        self.inc += 1
        self.points = np.concatenate((
            self.points,
            np.array(
                [[event.x,
                  event.y,
                  self.stroke_count]])), axis=0)

    def initialize_points(self):
        self.points = np.array([[-1, -1, -1]])
        self.stroke_count = -1
        self.inc = 0

    def reset(self):
        self.undo_stack = []
        self.redo_stack = []
        self.initialize_points()

    def mouse_up(self):
        # self.redo_stack.append(self.points)
        pass

    def click(self):
        self.stroke_count += 1
        self.undo_stack.append(self.points)
        self.last_inc = self.inc

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.points)
            self.points = self.undo_stack.pop()
            self.stroke_count = self.stroke_count - 1

        else:
            self.initialize_points()

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.points)
            self.points = self.redo_stack.pop()
            self.stroke_count = self.stroke_count + 1
