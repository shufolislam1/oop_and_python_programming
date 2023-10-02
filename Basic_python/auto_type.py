import pyautogui
from time import sleep

sleep(3)
for j in range(0,3):
    pyautogui.write('Hello world!', interval=0.25)
    pyautogui.press('enter')