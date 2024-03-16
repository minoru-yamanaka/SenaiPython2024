import keyboard
import time

keyboard.press("a")
time.sleep(1)
keyboard.release("a")
keyboard.press_and_release('\n, b, \n')
keyboard.write('python')
