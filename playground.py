import os
import pyautogui as gui
import pyperclip

date = gui.locateOnScreen('img/deliverdate.png',confidence=0.800)
gui.moveTo(date.left+date.width,date.top+date.height)
gui.dragTo(date.left+date.width+230,date.top+date.height,0.2)
gui.hotkey('ctrl','c')
gui.hotkey('alt','tab')
gui.press('left')
date = pyperclip.paste().replace('\n','').replace('\t','')
print(date[0:4]+'/'+date[5:7]+'/'+date[8:10])
gui.press('right')

