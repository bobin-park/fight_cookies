from SceneClass import *
from pico2d import *

def start_game():
    open_canvas()

    global screen
    screen = StartScene()

def update_screen():
    SceneManager.update(screen)


start_game()
while 1:
    update_screen()
    pass
