import pyautogui as auto
from time import sleep
import keyboard

while True:
    auto.write('your_text')
    auto.press('enter')
    sleep(0.1)
    if keyboard.is_pressed('escape'):
        while True:
            sleep(1)
