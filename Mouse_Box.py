CANVAS_H = 800

class Mouse:
    def __init__(self):
        self.mx,self.my =0,0
    def handle(self,event,imagebox):
        self.mx,self.my=event.x,CANVAS_H - event.y
        return imagebox.mouse(self.mx,self.my)


class ImageBox:
    def __init__ (self,image,x,y,w,h):
        self.image=image
        self.x,self.y=x,y
        self.w, self.h = w,h
    def draw(self):
        self.image.draw_to_origin(self.x,self.y,self.w,self.h)
    def mouse(self,mx,my):
        return self.x<=mx <=self.x+self.w and self.y<=my<=self.y+self.h
