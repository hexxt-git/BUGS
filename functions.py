from pyray import *
import math
import random
from inputs import *
from outputs import *

inputs = [ locX, locY, adjN, adjE, adjS, adjW, rdm, age, osc2, osc5, osc10, nearby3] #12
outputs = [ moveN, moveE, moveS, moveW, moveR, moveF, turn]#5

class Bug:
    def __init__(self, code, style):
        self.code = code
        self.style = style
        self.forward = 'NESW'[random.randint(0, 3)]

def generationGenerator( parents, count, w, h, complexity, mutation):
    #for the first generation or if there are not enough survivors
    while len(parents) < 20:
        code = []
        for synaps in range(complexity):
            code.append([random.randint( 0, len(inputs)-1), #input
            random.random()*6-3, #weight
            random.randint( 0, len(outputs)-1)]) # output
        style = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255]
        parents.append(Bug(code, style))
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
        #mixing two parents
        parent1 = parents[random.randint( 0, len(parents)-1)]
        parent2 = parents[random.randint( 0, len(parents)-1)]
        code = []
        style = []
        for synaps in range(complexity):
            parent = random.randint(1, 2)
            if parent == 1:
                code.append(parent1.code[synaps])
            if parent == 2:
                code.append(parent2.code[synaps])
        for channel in range( 0, 3):
            parent = random.randint(1, 3)
            if parent == 1:
                style.append(parent1.style[channel])
            if parent == 2:
                style.append(parent2.style[channel])
            if parent == 3:
                mix = math.floor((parent1.style[channel]+parent2.style[channel])/2)
                style.append(mix)
        #mutation
        for synaps in range(complexity):
            for value in range(3):
                if value == 0:
                    if random.random() < mutation:
                        code[synaps][value] = random.randint( 0, len(inputs)-1)
                if value == 1:
                    if random.random() < mutation:
                        code[synaps][value] = random.random()*6-3
                if value == 2:
                    if random.random() < mutation:
                        code[synaps][value] = random.randint( 0, len(outputs)-1)
        for channel in range( 0, 3):
                if random.random() < mutation:
                    style[channel] = random.randint( 0, 255)
        #appending the new born
        validated += 1
        print(style)
        children[x][y] = Bug( code, style)
    return children

def update(bugs, w, h, step, maxSteps):
    for x in range(w):
        for y in range(h):
            if bugs[x][y] != None:
                moves = [0] * len(outputs)
                for connection in bugs[x][y].code:
                    value = inputs[int(connection[0])](bugs, x, y, w, h, step, maxSteps) * connection[1]
                    moves[connection[2]] += value
                if abs(max(moves)) > 0.5:
                    outputs[moves.index(max(moves))](bugs, x, y, w, h)
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