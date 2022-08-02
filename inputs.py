import random
import math
from functions import *
#location x
def locX( bugs, bug, w, h, step, maxSteps):
    return bug.x / w
#location y
def locY( bugs, bug, w, h, step, maxSteps):
    return bug.y / h
#adjacent N
def adjN( bugs, bug, w, h, step, maxSteps):
    if bugAt( bugs, x, y-1) != None:
        return 1
    return 0
#adjacent E
def adjE( bugs, bug, w, h, step, maxSteps):
    if bugAt( bugs, x+1, y) != None:
        return 1
    return 0
#adjacent S
def adjS( bugs, bug, w, h, step, maxSteps):
    if bugAt( bugs, x, y+1) != None:
        return 1
    return 0
#adjacent W
def adjW( bugs, bug, w, h, step, maxSteps):
    if bugAt( bugs, x-1, y) != None:
        return 1
    return 0
#random
def rdm( bugs, bug, w, h, step, maxSteps):
    return random.random()
#random strong
def rdmStrong( bugs, bug, w, h, step, maxSteps):
    return random.randint( 0, 1)
#age
def age( bugs, bug, w, h, step, maxSteps):
    return step / maxSteps
#oscillator 2
def osc2( bugs, bug, w, h, step, maxSteps):
    return age % 2
#oscillator 5
def osc5( bugs, bug, w, h, step, maxSteps):
    return math.sin( bug.age * math.pi * 2 / 5) / 2 + 0.5
#oscillator 10
def osc10( bugs, bug, w, h, step, maxSteps):
    return math.sin( bug.age * math.pi * 2 / 10) / 2 + 0.5
#when these functions are called they take in the gen and current id as input and return a value from 0 to 1