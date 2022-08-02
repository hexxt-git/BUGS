from pyray import *
import math
import random
from functions import *
from inputs import *
from outputs import *

maxSteps = 1000
width = 1200
height = 660
res = 16
w = math.floor(width/res)
h = math.floor(height/res)

inputs = [ locX, locY, adjN, adjE, adjS, adjW, rdm, rdmStrong, age, osc2, osc5, osc10, osc20, on, off, half]
outputs = [ moveN, moveE, moveS, moveW, moveR]

bugs = generationGenerator( [0], 300, w, h, 0)
init_window( width, height, "BUGS")
step = 0
#set_target_fps(20)
while not window_should_close():
    step += 1
    for x in range(len(bugs)):
        for y in range(len(bugs[x])):
                bugs = moveR( bugs, x, y, w, h)
    render(bugs, res, w, h)

close_window()