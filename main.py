from SceneClass import *

def start_game():
    global screen
    screen = StartScene()

def update_screen():
    SceneManager.update(screen)

while 1:
    pass
