from SceneClass import *
from pico2d import *

class Mouse:
    def __init__(self):
        self.mx,self.my =0,0
    def handle(self,event,imagebox):
        mx,my=event.x,CANVAS_H - event.y
        if event.type == SDL_MOUSEBUTTONDOWN:
            self.imagebox.mouse(mx,my)


class ImageBox:
    def __init__ (self,image,x,y,w,h):
        self.image=image
        self.x,self.y=x,y
        self.w, self.h = w,h
    def draw(self):
        self.image.draw_to_origin(self.x,self.y,self.w,self.h)
    def mouse(self,mx,my):
        return self.x<=mx <=self.x+self.w and self.y<=my<=self.y+self.h
