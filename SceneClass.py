from ImageBox import *
from pico2d import *

CANVAS_W, CANVAS_H = 1350, 800
CX, CY = CANVAS_W//2, CANVAS_H//2
EXIT = object()
mouse = Mouse()

class BaceScene: #모든 화면이 공통적으로 수행하는 기능을 담는 클래스
    def __init__(self,scene):
        self.scene = scene

class SceneManager:
    def __init__(self, Scene):
        self.scene = Scene
        self.event =None

        self.START = StartScene
        self.CHAR = CharacterSelect
        self.COSTUME = CostumeSelect
        self.FIGHT = FightScene
        self.scene_flow = {
            self.START: {'NEXT': self.CHAR, 'BACK': EXIT},
            self.CHAR: {'NEXT': self.COSTUME, 'BACK': self.START},
            self.COSTUME: {'NEXT': self.FIGHT, 'BACK': self.CHAR},
            self.FIGHT: {'BACK': self.CHAR,'NEXT': self.START}}
    def handle(self,event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_n:
                self.event = 'NEXT'
            elif event.key == SDLK_b:
                self.event = 'BACK'
        if event.type ==SDL_MOUSEBUTTONDOWN or event.type == SDL_MOUSEBUTTONUP:
            self.scene.handle(event)
            print(event.x,event.y)
        self.change(self.event)


    def change(self, state_event):
        global GRunning
        if state_event in self.scene_flow[self.scene.__class__]:
            next_scene = self.scene_flow[self.scene.__class__][state_event]
            if next_scene != EXIT:
                self.scene = next_scene()
            elif next_scene == EXIT:
                close_canvas()
                sys.exit()
    def update(self):
        self.scene.update()
    def draw(self):
        clear_canvas()
        self.scene.background.draw(CX, CY)
        self.scene.draw()
        update_canvas()

class StartScene:
    def __init__(self):
        self.background = load_image('화면 리소스/시작 화면/background.png')
        self.title = load_image('화면 리소스/시작 화면/title.png')
        self.start = load_image('화면 리소스/시작 화면/start.png')
        self.exit = load_image('화면 리소스/시작 화면/exit.png')
        self.CCutter = load_image('화면 리소스/시작 화면/쿠키틀.png')

        self.start_btn = ImageBox( self.start ,CX - 150 - 200,  CY - CY / 4,  300,  100 )
        self.exit_btn = ImageBox( self.exit, CX - 100 + 200,   CY - CY / 4,  200, 100 )

    def draw(self):
        self.title.draw_to_origin(CX - 500, CY+CY/2, 1000, 150)
        self.CCutter.draw_to_origin(CX - 175 - 200, CY - CY/ 4-125, 350, 350)
        self.CCutter.draw_to_origin(CX - 175 + 200, CY - CY / 4-125, 350, 350)
        self.start_btn.draw()
        self.exit_btn.draw()

    def handle(self,event):
        self.start_btn

    def update(self):
        pass

class CharacterSelect:
    def __init__(self):
        self.background = load_image('화면 리소스/선택 화면/background.png')
    def draw(self):
        pass

    def update(self):
        pass

class CostumeSelect:
    def __init__(self):
        self.background = load_image('화면 리소스/선택 화면/background.png')
    def draw(self):
        pass
    def update(self):
        pass

class FightScene:
    def __init__(self):
        self.background = load_image('화면 리소스/플레이 화면/마녀배경.png')
    def draw(self):
        pass
    def update(self):
        pass


