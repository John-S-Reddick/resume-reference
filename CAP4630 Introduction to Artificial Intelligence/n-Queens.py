from collections import deque
from PIL import Image
import numpy as np
from math import *
import random



#Settings
POPS = 16


size = 0
maxscore = 0
bias = 0

pstring = ""


class Genome(object):
    def __init__(self):
        self.genes = np.random.randint(0, size, size)
        self.fitness = maxscore


    def mutate(self):
        self.genes[random.randrange(0, size)] = random.randrange(0, size)

    def compete(self):
        self.fitness = maxscore
        for i in range(size):
            for j in range(i + 1, size):
                if self.genes[i] == self.genes[j] or j - i == abs(self.genes[j] - self.genes[i]):
                        self.fitness -= 1

        return self.fitness - bias
    

    def outty(self):
        print(self.genes)

    

    def disp(self):
        len = self.genes.size

        x = ""
        for i in range(len):
            x += "\n"
            for b in range(len):
                if i != self.genes[b]:
                    x += " _ "
                else:
                    x += " Q "
                
        return x

        

        

class GenePool(object):
    def __init__(self):
        self.currGen = []
        self.nextGen = []

        self.currScore = []
        self.nextScore = []

        self.best = None

        self.generation = 0


        for i in range(POPS):
            creature = Genome()
            self.currGen.append(creature)
            self.currScore.append(creature.compete())



    def identmax(self):
        for i in self.currGen:
            if(i.compete() + bias == maxscore):
                print(i.genes)

    def evolve(self):
        sum = 0
        self.generation += 1
        
        self.best = self.currGen[0]
        for i in self.currGen:
            if i.compete() > self.best.compete():
                self.best = i

        print(self.generation, " : ", self.best.genes)


        for i in range(int(POPS / 2)):
            self.breed()

        
        
        self.currGen = self.nextGen
        self.nextGen = []

        self.currScore = self.nextScore
        self.nextScore = []

    
        return self.best

    def breed(self):
        beb1 = Genome()
        beb2 = Genome()

        sum = 0

        for i in self.currScore:
            sum += i

        par1 = 0
        par2 = 0

        rand1 = 0
        rand2 = 0

        while(rand1 != rand2):
            par1 = 0
            par2 = 0
            rand1 = random.randrange(0, sum)
            rand2 = random.randrange(0, sum)

            for i in self.currScore:
                if rand1 < sum:
                    par1 += 1

                if rand1 < sum:
                    par1 += 1
            
                sum -= i

        beb1.genes = self.currGen[par1].genes
        beb2.genes = self.currGen[par2].genes

        for i in range(random.randrange(0, size)):
            chrom = beb1.genes[i]
            beb1.genes[i] = beb2.genes[i]
            beb2.genes[i] = chrom
        
        beb1.mutate()
        beb2.mutate()

        self.nextGen.append(beb1)
        self.nextScore.append(beb1.compete())

        self.nextGen.append(beb2)
        self.nextScore.append(beb2.compete())



if __name__ == "__main__":
    size = 4
    while(3 < size < 21):
        maxscore = ((size * size) - size)/2
        bias = maxscore / 1.5
        doug = GenePool()

        best = Genome()
        generation = 0
        while best.compete() + bias != maxscore:
            best = doug.evolve()
            

        print("\n", doug.generation + 1, ": Final:")
        print(best.disp())

        print("Input board size, or type 0 to quit")
        size = int(input("Board size:"))

    
