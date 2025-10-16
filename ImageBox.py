from SceneClass import *
from pico2d import *

class ImageBox:
    def __init__ (self,image,x,y,w,h):
        self.image=image
        self.x,self.y=x,y
        self.w, self.h = w,h