import math
import random
from functions import *

#move N
def moveN( bugs, x, y, w, h):
    if y-1 < 0:
        return bugs
    if bugs[x][y-1] != None:
        return bugs
    if y == 0:
        return bugs
    temp = bugs[x][y-1]
    bugs[x][y-1] = bugs[x][y]
    bugs[x][y] = temp
    return bugs
#move E
def moveE( bugs, x, y, w, h):
    if x+1 >= len(bugs):
        return bugs
    if bugs[x+1][y] != None:
        return bugs
    if x == w:
        return bugs
    temp = bugs[x+1][y]
    bugs[x+1][y] = bugs[x][y]
    bugs[x][y] = temp
    return bugs
#move S
def moveS( bugs, x, y, w, h):
    if y+1 >= len(bugs[0]):
        return bugs
    if bugs[x][y+1] != None:
        return bugs
    if y == h:
        return bugs
    temp = bugs[x][y+1]
    bugs[x][y+1] = bugs[x][y]
    bugs[x][y] = temp
    return bugs
#move W
def moveW( bugs, x, y, w, h):
    if x-1 < 0:
        return bugs
    if bugs[x-1][y] != None:
        return bugs
    if x == 0:
        return bugs
    temp = bugs[x-1][y]
    bugs[x-1][y] = bugs[x][y]
    bugs[x][y] = temp
    return bugs
#move R
def moveR( bugs, x, y, w, h):
    direction = random.randint( 1, 4)
    if direction == 1:
        return moveN( bugs, x, y, w, h)
    if direction == 2:
        return moveE( bugs, x, y, w, h)
    if direction == 3:
        return moveS( bugs, x, y, w, h)
    if direction == 4:
        return moveW( bugs, x, y, w, h)
    return bugs