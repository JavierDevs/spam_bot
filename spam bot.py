import pyautogui as auto
from time import sleep

while True:
    auto.write('your_text')
    auto.press('enter')
    sleep(0.1)