import math
import random
from functions import *

def moveN( bugs, x, y, w, h):
    if y <= 0:
        return bugs
    if bugs[x][y-1] != None:
        return bugs
    temp = bugs[x][y-1]
    bugs[x][y].forward = 'N'
    bugs[x][y-1] = bugs[x][y]
    bugs[x][y] = temp
    return bugs
def moveE( bugs, x, y, w, h):
    if x >= w-1:
        return bugs
    if bugs[x+1][y] != None:
        return bugs
    temp = bugs[x+1][y]
    bugs[x][y].forward = 'E'
    bugs[x+1][y] = bugs[x][y]
    bugs[x][y] = temp
    return bugs
def moveS( bugs, x, y, w, h):
    if y >= h-1:
        return bugs
    if bugs[x][y+1] != None:
        return bugs
    temp = bugs[x][y+1]
    bugs[x][y].forward = 'S'
    bugs[x][y+1] = bugs[x][y]
    bugs[x][y] = temp
    return bugs
def moveW( bugs, x, y, w, h):
    if x <= 0:
        return bugs
    if bugs[x-1][y] != None:
        return bugs
    temp = bugs[x-1][y]
    bugs[x][y].forward = 'W'
    bugs[x-1][y] = bugs[x][y]
    bugs[x][y] = temp
    return bugs
def moveR( bugs, x, y, w, h):
    direction = random.randint( 1, 4)
    if direction == 1:
        return moveW( bugs, x, y, w, h)
    if direction == 2:
        return moveS( bugs, x, y, w, h)
    if direction == 3:
        return moveE( bugs, x, y, w, h)
    if direction == 4:
        return moveN( bugs, x, y, w, h)
    return bugs
def moveF( bugs, x, y, w, h):
    if bugs[x][y].forward == 'N':
        return moveN(bugs, x, y, w, h)
    if bugs[x][y].forward == 'E':
        return moveE(bugs, x, y, w, h)
    if bugs[x][y].forward == 'S':
        return moveS(bugs, x, y, w, h)
    if bugs[x][y].forward == 'W':
        return moveW(bugs, x, y, w, h)
    return bugs
def turn( bugs, x, y, w, h):
    if bugs[x][y].forward == 'N':
        bugs[x][y].forward = 'S'
    if bugs[x][y].forward == 'E':
        bugs[x][y].forward = 'W'
    if bugs[x][y].forward == 'S':
        bugs[x][y].forward = 'N'
    if bugs[x][y].forward == 'W':
        bugs[x][y].forward = 'E'
    return bugs