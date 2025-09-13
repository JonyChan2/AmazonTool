import openpyxl as pxl
import tkinter as tk
from tkinter import filedialog
import pyautogui as gui
from time import sleep
import pyperclip
import keyboard as kbd

def get_user_name():
    gui.hotkey('ctrl','c')
    gui.click(gui.locateOnScreen('img/ziniaologo.png'))
    gui.hotkey('ctrl','0')
    print('Order detail:'+pyperclip.paste().replace('\n',''))
    gui.hotkey('ctrl','t')
    gui.press('tab',3)
    gui.write('https://sellercentral.amazon.com/orders-v3/order/' + pyperclip.paste())
    gui.press('enter')

    #等待页面加载
    while (1):
            try:
                gui.locateOnScreen('img/address.png')
                break
            except:
                print('not found, retrying...')
                sleep(0.1)

    gui.moveTo(1800,540)
    gui.keyDown('shift')
    gui.scroll(-400)
    gui.keyUp('shift')
    buyer = gui.center(gui.locateOnScreen('img/contact_buyer.png'))
    old_clip = pyperclip.paste().replace('\t','').replace('\n','')
    gui.moveTo(buyer.x+30,buyer.y)
    gui.dragTo(buyer.x+150,buyer.y,0.3)
    pyperclip.copy('')
    gui.hotkey('ctrl','c')
    gui.hotkey('ctrl','w')

    gui.hotkey('alt','tab')
    gui.press('tab')
    gui.write(pyperclip.paste().replace('\t','').replace('\n',''))
    gui.press('enter')

def email_user():
    gui.hotkey('ctrl','c')
    gui.click(gui.locateOnScreen('img/ziniaologo.png'))
    gui.hotkey('ctrl','0')
    print('Order detail:'+pyperclip.paste().replace('\n',''))
    gui.hotkey('ctrl','t')
    gui.press('tab',3)
    site = 'https://sellercentral.amazon.com/messaging/contact?orderID='+pyperclip.paste().replace('\t','').replace('\n','')
    site += '&marketplaceID='
    if pyperclip.paste()[1]=='1':
        site+='ATVPDKIKX0DER'
    elif pyperclip.paste()[1]=='7':
        sit+='A2EUQ1WTGCTBG2'
    gui.write(site)
    gui.press('enter')

while (kbd.is_pressed('ctrl+shift+s')!=1):
     sleep(0.1)
sleep(1)
'''
while (1):
'''
email_user()