from pynput.keyboard import Key, Controller
from time import sleep
keyboard = Controller()
x = 0
sleep(1)
while x < 4:

    for num in range(80):
        keyboard.press(".")
        sleep(.1)
    keyboard.release(".")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    x += 1
