from SceneClass import *
from pico2d import *

def start_game():
    open_canvas()

    global screen
    global manager
    screen = StartScene()
    manager = SceneManager(screen)

def update_screen():
    manager.update()


start_game()
while 1:
    update_screen()
    pass
