from pico2d import *
CANVAS_W, CANVAS_H = 1350, 800
CX, CY = CANVAS_W//2, CANVAS_H//2
EXIT = object()

class BaceScene: #모든 화면이 공통적으로 수행하는 기능을 담는 클래스
    def __init__(self,scene):
        self.scene = scene

class SceneManager:
    def __init__(self, Scene):
        self.scene = Scene  # 현재 장면이 무슨 장면인지 받음
        self.event =None
        # self.stateM = StateManager()

        self.START = StartScene
        self.CHAR = CharacterSelect
        self.COSTUME = CostumeSelect
        self.FIGHT = FightScene

        # self.EXIT =
        self.scene_flow = {
            self.START: {'NEXT': self.CHAR, 'BACK': EXIT},
            self.CHAR: {'NEXT': self.COSTUME, 'BACK': self.START},
            self.COSTUME: {'NEXT': self.FIGHT, 'BACK': self.CHAR},
            self.FIGHT: {'BACK': self.CHAR}}
        # self.background = scene.background
    def handle(self,event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_n:
                self.event = 'NEXT'
            elif event.key == SDLK_b:
                self.event = 'BACK'
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
        # print('background image:', self.background)
    def draw(self):
        self.title.draw_to_origin(CX - 500, CY+CY/2, 1000, 150)
        self.CCutter.draw_to_origin(CX - 175 - 200, CY - CY/ 4-125, 350, 350)
        self.CCutter.draw_to_origin(CX - 175 + 200, CY - CY / 4-125, 350, 350)
        self.start.draw_to_origin(CX - 150-200, CY - CY /4, 300, 100)
        self.exit.draw_to_origin(CX - 100+ 200, CY - CY / 4, 200, 100)

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


