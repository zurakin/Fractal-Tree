import cv2
import random
from math import pi
import numpy as np
import branch
import constantes

##create black background
img = np.zeros((constantes.height,constantes.width) ,dtype = np.uint8)


def execute():
    branches = [branch.Branch(coords = (int(constantes.width/2),int(constantes.height)), length = constantes.length, angle = pi/2 ,thikness = constantes.thikness)]
    new_branches = []
    tscale = constantes.tscale
    while True:
        for br in branches:
            if br.length <1:
                return 'branch became too small'
            br.draw(img)
            #branch to the right
            new_branches.append(branch.Branch(coords = br.end,
            length = br.length*constantes.length_multiplier,
            angle = br.angle + constantes.added_angle,
            thikness = br.thikness*constantes.thikness_multiplier))
            #branch to the left
            new_branches.append(branch.Branch(coords = br.end,
            length = br.length*constantes.length_multiplier,
            angle = br.angle - constantes.added_angle,
            thikness = br.thikness*constantes.thikness_multiplier))

            cv2.imshow('tree',img)
            key = cv2.waitKey(tscale)
            if key == 27:
                return 'user pressed esc button'
        if tscale >2:
            tscale = int(tscale/2)
        branches = new_branches.copy()
        new_branches = []

print(execute())
