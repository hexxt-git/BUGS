from pyray import *
import math
import random
from functions import *
from inputs import *
from outputs import *

with open('results.txt', 'w') as textFile:
    textFile.write('----EVOLUTION----')

maxSteps = 1000
width = 1202
height = 660
res = 16
w = math.floor(width/res)
h = math.floor(height/res)

bugs = generationGenerator( [], 500, w, h, 10, 1)
init_window( width, height, "BUGS")
step = 0
generation = 0
#set_target_fps(30)
while not window_should_close():
    step += 1
    bugs = update(bugs, w, h, step, maxSteps)
    render(bugs, res, generation)
    #generating a new generation every 1k step
    if step == 1000:
        generation += 1
        step = 0
        parents = []
        for x in range(len(bugs)):
            for y in range(12):
                if bugs[x][y] != None:
                    parents.append(bugs[x][y])
        bugs = generationGenerator( parents, 500, w, h, 10, 0.05)
        print('gen '+str(generation-1) + ': ' + str(len(parents)) + ', '+ str(math.floor(len(parents)/500*100*1000)/1000) + '%')
        f = open("results.txt", "a")
        f.write('\ngen '+str(generation-1) + ': ' + str(math.floor(len(parents)/500*100*1000)/1000) + '%')
close_window()