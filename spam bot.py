import pyautogui
import appJar
from time import sleep
import keyboard

def buttonPress(button):
    if(button == "Start"):
        amount = int(app.getEntry("amount"))
        text = str(app.getEntry("text"))
        sleep(3)
        for _ in range(amount):
            pyautogui.write(text,interval=0)
            pyautogui.press('enter')
    if(button == "End"):
        while keyboard.is_pressed('enter')==True:
            pyautogui.sleep

app = appJar.gui("Spam Bot")
app.setSize("600x500")
app.setSticky("new")
app.addLabel("Spam Bot", row=0)
app.setSticky("new")
app.addLabel("Number of times spammed",row=1)
app.addEntry("amount",row=2)
app.setSticky("new")
app.addLabel("Spammed text",row=3)
app.addEntry("text", row=4)
app.setSticky("new")
app.addButton("Start", buttonPress, row=5)
app.setSticky("new")
app.addLabel("Click on where you want to spam after pressing start",row=6)
app.setSticky("new")
app.addButton("End", buttonPress, row=7)
app.go()
