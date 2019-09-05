import cv2
import random
from math import pi
import numpy as np
import branch
import constantes

changed = False


def nothing(x):
    global changed
    changed = True

##create black background
def execute():
    cv2.destroyAllWindows()
    cv2.namedWindow('tree')
    img = np.zeros((constantes.height,constantes.width) ,dtype = np.uint8)
    cv2.createTrackbar('Curviness','tree',0,100,nothing)
    branches = [branch.Branch(coords = (
    int(constantes.width/2),int(constantes.height)),
    length = constantes.length, angle = pi/2 ,thikness = constantes.thikness)]
    new_branches = []
    tscale = constantes.tscale
    while True:
        global changed
        for br in branches:
            if br.length <5:
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
                return 'User pressed ESC button'
            if changed:
                cur = cv2.getTrackbarPos('Curviness','tree')
                constantes.added_angle = cur * pi /50
                changed = False
            if key == 13:
                execute()
                return 'User pressed ESC button'

        if tscale >2:
            tscale = int(tscale/2)
        branches = new_branches.copy()
        new_branches = []

print(execute())
cv2.destroyAllWindows()
