from pyray import *
import math
import random
from functions import *
from inputs import *
from outputs import *

with open('results.txt', 'w') as textFile:
    textFile.write('----SURVIVAL RATES:----')

maxSteps = 1000
width = 960
height = 600
res = 16
w = math.floor(width/res)
h = math.floor(height/res)

bugs = generationGenerator( [], 200, w, h, 10, 1)
init_window( width, height, "BUGS")
step = 0
generation = 0
data = []
state = 1
#set_target_fps(20)
while not window_should_close():
    step += 1
    bugs = update(bugs, w, h, step, maxSteps)
    render(bugs, res, generation, state)
    #generating a new generation every 1k step
    if is_key_pressed(KEY_SPACE):
            state *= -1
            if state == 1:
                f.write('--changed selection side to east--')
            else:
                f.write('--changed selection side to west--')
    if step == 1000:
        generation += 1
        step = 0
        parents = []
        for x in range(len(bugs)):
            for y in range(len(bugs[0])):
                if bugs[x][y] != None:
                    if state == 1:
                        if (x >= w-8 )&( x <= w):
                            if (y >= 0 )&( y <= h):
                                parents.append(bugs[x][y])
                    if state == -1:
                        if (x >= 0 )&( x <= 8):
                            if (y >= 0 )&( y <= h):
                                parents.append(bugs[x][y])
        bugs = generationGenerator( parents, 200, w, h, 10, 0.0005)
        f = open("results.txt", "a")
        f.write('\ngen '+str(generation) + ' survivors: ' + str(math.floor(len(parents)/200*100*100)/100) + '%')
        data.append(len(parents))
close_window()

#something is really broken here idk what