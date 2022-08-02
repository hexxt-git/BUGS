import random
import math
from functions import *
#location x
def locX( bugs, x, y, w, h, step, maxSteps):
    return x / w
#location y
def locY( bugs, x, y, w, h, step, maxSteps):
    return y / h
#adjacent N
def adjN( bugs, x, y, w, h, step, maxSteps):
    if y != 0:
        if bugs[x][y-1] != None:
            return 1
    return 0
#adjacent E
def adjE( bugs, x, y, w, h, step, maxSteps):
    if x != w-1:
        if bugs[x+1][y] != None:
            return 1
    return 0
#adjacent S
def adjS( bugs, x, y, w, h, step, maxSteps):
    if y != h-1:
        if bugs[x][y+1] != None:
            return 1
    return 0
#adjacent W
def adjW( bugs, x, y, w, h, step, maxSteps):
    if x != 0:
        if bugs[x-1][y] != None:
            return 1
    return 0
#random
def rdm( bugs, x, y, w, h, step, maxSteps):
    return random.random()
#age
def age( bugs, x, y, w, h, step, maxSteps):
    return step / maxSteps
#oscillator 2
def osc2( bugs, x, y, w, h, step, maxSteps):
    return step % 2
#oscillator 5
def osc5( bugs, x, y, w, h, step, maxSteps):
    return math.sin( step * math.pi * 2 / 5) / 2 + 0.5
#oscillator 10
def osc10( bugs, x, y, w, h, step, maxSteps):
    return math.sin( step * math.pi * 2 / 10) / 2 + 0.5
#when these functions are called they take in the gen and current id as input and return a value from 0 to 1