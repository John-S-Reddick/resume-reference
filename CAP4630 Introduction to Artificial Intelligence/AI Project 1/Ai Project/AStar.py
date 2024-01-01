from queue import PriorityQueue
from PIL import Image
import numpy as np
from math import sqrt, pow



#Settings
IMAGE_NAME  = "Geometry.png"
OUTPUT_NAME = "Output"
DURATION    = 5
BUFFER = 100
RATIO = 1

# Pixel Types
START       = 0
DISCOVERED  = 1
EXPLORING   = 2
EXPLORED    = 3
GOAL        = 4
WALL        = 5

#Color Definitions
RED     = (255, 0, 0)
GREEN   = (0, 255, 0)
BLUE    = (0, 0, 255)
LBLUE    = (100, 100, 255)
YELLOW  = (255, 255, 0)
BLACK   = (0, 0, 0)
GRAY    = (180, 180, 230)
PURPLE  = (95, 0, 125)

#Pallete dictionary
PALLETE ={
    START       : BLUE,
    DISCOVERED  : GRAY,
    EXPLORING   : YELLOW,
    EXPLORED    : LBLUE,
    GOAL        : GREEN,
    WALL        : PURPLE
}


class Node(object):
    def __init__(self, parent, x, y):
        self.children = []
        self.parent = parent
        self.x = x
        self.y = y

        self.dist = 1000

        if(parent != None):
            self.type = DISCOVERED
        else:
            self.type = START

        
        

    def cost(self):
        if self.type != START:
            return + self.parent.cost() + sqrt(pow((self.x - self.parent.x), 2) + pow((self.y - self.parent.y), 2))
        else:
            return 0
        
    def func(self):
        return self.cost() + self.dist
        

    def getStart(self):
        if(self.parent != None):
            return self.parent
        else:
            return self
        
    def patTest(self, parent):
        if self.parent != None:
            if parent.cost() < self.parent.cost():
                self.parent = parent
                self.parent.children.append(self)
                return True
        return False
            

    def __lt__(self, other):
        return self.func() < other.func()


class Path(object):
     def __init__(self, start, type):
        self.type = type
        self.start = start
        self.end = start.getStart()

        self.list =[]

        temp = start

        while temp != None:
            self.list.append(temp)
            temp = temp.parent

class Grid(object):
    def __init__(self, image):
        self.image_name = image
        self.img = Image.open(self.image_name)
        self.img_arr = np.array(self.img, np.uint8)
        self.width = self.img.size[0]
        self.height = self.img.size[1]

        self.Grid = np.ones((self.height, self.width))

        for x in range (self.width):
            for y in range(self.height):
                c = self.img_arr[y][x]

                if c[0] < 100 and c[1] < 100 and c[2] < 100:
                    self.Grid[y][x] = WALL
                elif c[0] == BLUE[0] and c[1] == BLUE[1] and c[2] == BLUE[2]:
                    self.Grid[y][x] = START
                    self.startx = x
                    self.starty = y
                elif c[0] == GREEN[0] and c[1] == GREEN[1] and c[2] == GREEN[2]:
                    self.Grid[y][x] = GOAL
                    self.goalx = x
                    self.goaly = y
                    

    def getType(self, exp):
        exp.type = self.Grid[exp.y][exp.x]
        if exp.type == DISCOVERED:
            self.Grid[exp.y][exp.x] = EXPLORED
        
class GifOut(object):
    def __init__(self, base):
        self.frames = []
        self.currFrame = base
        self.base = base
        self.count = 0
        self.mod = BUFFER

        self.size = base.size

    def drawPix(self, exp, color):
        if 0 < exp.x < self.size[0] and 0 < exp.y < self.size[1]:
            self.currFrame.putpixel((exp.x, exp.y), color)

    def drawPix2(self, exp):
        self.drawPix(exp, PALLETE[exp.type])

    def drawPath(self, p, color):
        for e in p.list:
            self.drawPix(e, color)

    def drawPath2(self, p):
        self.drawPath(p, PALLETE[p.type])
            

    def newFrame(self):
        tFrame = Image.new('RGB', (self.size))
        tFrame.paste(self.currFrame)
        self.currFrame = tFrame
        self.count += 1
        if self.count == self.mod:
            self.snap()

    def snap(self):
        self.frames.append(self.currFrame)
        self.count = 0
        self.mod + BUFFER

    def output(self):
        self.currFrame.save(OUTPUT_NAME + ".png")
        self.currFrame.show()
        self.frames[0].save(OUTPUT_NAME + ".gif",
            save_all = True, append_images = self.frames[1:], 
           optimize = True, duration = DURATION)

class Tree(object):
    
    def __init__(self, IMAGE_NAME): 
        self.grid = Grid(IMAGE_NAME)

        self.width = self.grid.width
        self.height = self.grid.height
        

        self.max = self.width * self.height

        self.gif = GifOut(self.grid.img)

        self.vistedQueue ={}
        self.priorityQueue = PriorityQueue()

        self.start = Node(None, self.grid.startx, self.grid.starty)
        exp = self.start
        self.currPath = Path(exp, BLUE)

        self.priorityQueue.put(exp)
        i = 0

        while exp.type != GOAL and i < self.max * RATIO:
            i += 1
            exp = self.priorityQueue.get()
            print(i, "/", self.max,  100 * i / self.max, "\t", exp.x, exp.y, "\t", exp.func())
            self.currPath.type = EXPLORED
            self.gif.drawPath2(self.currPath)
            self.vistedQueue[(exp.x,exp.y)] = exp

            if exp.type == DISCOVERED:
                self.currPath = Path(exp, EXPLORING)
                self.gif.drawPath2(self.currPath)
                exp.type = EXPLORED
            
            elif exp.type == GOAL:
                self.currPath = Path(exp, GOAL)
                self.gif.drawPath2(self.currPath)

            #print("Fuck")
            for x in range (-1, 2):
                for y in range (-1, 2):
                    n = Node(exp, exp.x + x, exp.y + y)
                    if (0 < n.y < self.grid.height) and (0 < exp.x + n.x < self.grid.width):
                        if(n.x, n.y) not in self.vistedQueue.keys():
                            n.dist = sqrt(pow((self.grid.goaly - n.y), 2) + pow((self.grid.goalx - n.x), 2))
                            self.grid.getType(n)                           
                            if n.type != WALL and n.type != EXPLORED:                                
                                self.priorityQueue.put(n)                      
                            else:
                                n.dist == 2 * self.max
                        else:
                            n = self.vistedQueue[(exp.x,exp.y)]
                            if n.patTest(exp):
                                self.priorityQueue.put(n)
                        self.gif.drawPix2(n)
                                    
            self.gif.newFrame()
            

        self.gif.output()

            
        




if __name__ == "__main__":
    Astar = Tree(IMAGE_NAME)
    print("Done")
