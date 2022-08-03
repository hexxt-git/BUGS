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

bugs = generationGenerator( [], 200, w, h, 5, 0.01)
init_window( width, height, "BUGS")
step = 0
set_target_fps(30)
while not window_should_close():
    step += 1
    bugs = update(bugs, w, h, step, maxSteps)
    render(bugs, res)

close_window()