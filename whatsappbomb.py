import random
import pyautogui as pg
import webbrowser as wb
import time
wb.open("https://web.whatsapp.com")
enemy=('spam message')
time.sleep(40)
for i in range(100):
    a=random.choice(enemy)
    pg.write("you are " + a)
    pg.press('enter')