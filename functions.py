from pyray import *
import math
import random
from inputs import *
from outputs import *

inputs = [ locX, locY, adjN, adjE, adjS, adjW, rdm, age, osc2, osc5, osc10] #11
outputs = [ moveN, moveE, moveS, moveW, moveR]#5

class Bug:
    def __init__(self, code):
        self.code = code
        self.style = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255]

def generationGenerator( parents, count, w, h, mutation):
    #making an empty 2D list
    children = []
    for x in range(w):
        children.append([])
        for y in range(h):
            children[int(x)].append(None)
    #filling it with children
    validated = 0
    while validated < count:
        #finding a position
        x = random.randint( 0, w-1)
        y = random.randint( 0, h-1)
        while children[x][y] != None:
            x = random.randint( 0, w-1)
            y = random.randint( 0, h-1)
            print(children[x][y])
        #mixing two parents
        parent1 = parents[random.randint( 0, len(parents)-1)]
        parent2 = parents[random.randint( 0, len(parents)-1)]
        code = random.random()
        #mutating the code
        code = random.random()
        #appending the new born
        validated += 1
        children[x][y] = Bug(code)
    return children

def update(bugs, w, h, step, maxSteps):
    for x in range(w):
        for y in range(h):
            for i in inputs:
                i( bugs, x, y, w, h, step, maxSteps)
            moveR(bugs, x, y, w, h)
    return bugs

def render(bugs, res):
    begin_drawing()
    clear_background(Color( 30, 30, 50, 255))
    for x in range(len(bugs)):
        for y in range(len(bugs[x])):
            if bugs[x][y] != None:
                draw_circle( x*res + int(res/2), y*res + int(res/2), res/2, Color( bugs[x][y].style[0], bugs[x][y].style[1], bugs[x][y].style[2], 255))
    draw_fps( 5, 5)
    end_drawing()