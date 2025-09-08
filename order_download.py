#collect order
import pyautogui as gui
from time import sleep
import os

logocord = gui.locateOnScreen('img/ziniaologo.png')
x, y = gui.center(logocord)

gui.click(x,y)
gui.hotkey('ctrl','t')
gui.press('tab',3)
gui.write('https://sellercentral.amazon.com/reportcentral/FlatFileAllOrdersReport/1')
gui.press('enter')
sleep(2)
gui.hotkey('ctrl','0')
while (1):
    try:
        gui.click(gui.center(gui.locateOnScreen('img/lastday.png')))
        break
    except:
        print('not found, retrying...')
        sleep(1)
gui.press('down')
gui.press('enter')
gui.click(gui.center(gui.locateOnScreen('img/ask_download.png')))
gui.keyDown('shift')
gui.scroll(-400)
gui.keyUp('shift')
gui.scroll(-400)
print('Wait for it to finish',end='')
sleep(1)
wfd = 'Waiting for download'
while (1):
    try:
        down = gui.locateOnScreen('img/file_download.png')
        break
    except:
        sleep(1)
        wfd += '.'
        print('\r'+wfd,end='')

x, y = gui.center(down)
gui.click(x-10,y+15)
sleep(2)
gui.press('enter')
print('Download Complete!')
