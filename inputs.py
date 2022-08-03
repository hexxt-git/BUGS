import random
import math
from functions import *
def locX(bugs, x, y, w, h, step, maxSteps):
    return x / w
def locY(bugs, x, y, w, h, step, maxSteps):
    return y / h
def adjN(bugs, x, y, w, h, step, maxSteps):
    if y != 0:
        if bugs[x][y-1] != None:
            return 1
    return 0
def adjE(bugs, x, y, w, h, step, maxSteps):
    if x != w-1:
        if bugs[x+1][y] != None:
            return 1
    return 0
def adjS(bugs, x, y, w, h, step, maxSteps):
    if y != h-1:
        if bugs[x][y+1] != None:
            return 1
    return 0
def adjW(bugs, x, y, w, h, step, maxSteps):
    if x != 0:
        if bugs[x-1][y] != None:
            return 1
    return 0
def rdm(bugs, x, y, w, h, step, maxSteps):
    return random.random()
def age(bugs, x, y, w, h, step, maxSteps):
    return step / maxSteps
def osc2(bugs, x, y, w, h, step, maxSteps):
    return step % 2
def osc5(bugs, x, y, w, h, step, maxSteps):
    return math.sin( step * math.pi * 2 / 5) / 2 + 0.5
def osc10(bugs, x, y, w, h, step, maxSteps):
    return math.sin( step * math.pi * 2 / 10) / 2 + 0.5
def nearby3(bugs, x, y, w, h, step, maxSteps):
    count = -1
    for x1 in range(x-1, x+1):
        for y1 in range(y-1, y+1):
            if x1 < w:
                if y1 < h:
                    if x1 >= 0:
                        if y1 >= 0:
                            if bugs[x1][y1] != None:
                                count += 1
    return count/8