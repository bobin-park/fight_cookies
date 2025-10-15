from SceneClass import *
from pico2d import *

#화면 크기 : 1400*800
def start_game():
    open_canvas(CANVAS_W, CANVAS_H)

    global screen
    global manager
    screen = StartScene()
    manager = SceneManager(screen)

def handle_event():
    for event in get_events():
        # print("event", event)
        manager.handle(event)

def update_screen():
    manager.update()
    manager.draw()

# 코드 실행 시작================================
start_game()
while 1:
    handle_event()
    update_screen()
    delay(0.01)
close_canvas()