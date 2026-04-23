# from pynput.mouse import Controller
# def controlMouse():
#     mouse = Controller()
#     mouse.position = (621, 536)
# #controlMouse()

from pynput.mouse import Listener

def writeToFile(x, y):
    print(f"position of current mouse ({x}, {y})")
    # with open("log.txt", "a") as a:
    #     a.write(keyData)


with Listener(on_click=writeToFile) as L:
    L.join()