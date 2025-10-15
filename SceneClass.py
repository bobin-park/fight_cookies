from pico2d import load_image
from pico2d import *
CANVAS_W, CANVAS_H = 1350, 800
CX, CY = CANVAS_W//2, CANVAS_H//2

class BaceScene: #모든 화면이 공통적으로 수행하는 기능을 담는 클래스
    def __init__(self,scene):
        self.scene = scene

class SceneManager:
    def __init__(self, scene):
        self.scene = scene  # 현재 장면이 무슨 장면인지 받음
        # self.background = scene.background
    def handle(self):
        pass
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
        print('background image:', self.background)
    def draw(self):
        print("draw StartScene")
    def update(self):
        pass

class CharacterSelect:
    def __init__(self):
        pass
    def draw(self):
        print("draw CharacterSelect")
    def update(self):
        pass

class CostumeSelect:
    def __init__(self):
        pass
    def draw(self):
        print("draw CostumeSelect")
    def update(self):
        pass

class FightScene:
    def __init__(self):
        pass
    def draw(self):
        print("draw FightScene")
    def update(self):
        pass
