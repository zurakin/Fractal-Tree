import cv2
from math import cos , sin , pi

class Branch:
    def __init__(self,coords, length,angle,thikness):
        self.start = coords
        self.length = length
        self.end = (int(sin(-angle+pi/2) * length +coords[0]),int(-cos(-angle+pi/2) * length + coords[1]))
        self.thikness = thikness
        self.angle = angle

    def draw(self,background):
        cv2.line(background ,self.start,self.end,255,int(self.thikness)+1)
