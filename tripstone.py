# This is a python script for controlling ziniao browser
import pyautogui as gui
import tkinter
import sys
import keyboard as kbd
import pyperclip #Reading info from clipboard
from time import sleep

'''
# Search
gui.keyDown('ctrl')
gui.press('f')
gui.keyUp('ctrl')
'''
logocord = gui.locateOnScreen('img/ziniaologo.png')
x, y = gui.center(logocord)
email=[
'Subject: OUTOHOME Order Confirmation & Support Commitment\n\n\
Dear ',
',\n\n\
Thank you for purchasing OUTOHOME products on Amazon.\n\n\
We stand by our product quality and your satisfaction. Should any issues arise during product usage, contact us directly via Amazon Messages. Our support team will provide prompt assistance within 24 hours.\n\n\
We value your trust in OUTOHOME.\n\n\
Sincerely,\n\
OUTOHOME Team'
]

def new_tab():
    mouse = gui.position()
    gui.click(x,y)
    gui.moveTo(mouse)
    gui.keyDown('ctrl')
    gui.press('t')
    gui.keyUp('ctrl')
    gui.press('tab',3)

# Use paste() to store accelerate input speed.
def paste(coontent):
    og = pyperclip.paste()
    pyperclip.copy(coontent)
    gui.hotkey('ctrl','v')
    pyperclip.copy(og)

# Fast input
# use a/s/z/x instead
print('Use hotkey below to quick access:\n\
ctrl+shift+x = removal id\n\
ctrl+shift+z = order detail\n\
ctrl+shift+d = email template input(EN)\n\
ctrl+shift+s = contact shopper')
while (1):
    if kbd.is_pressed('ctrl+shift'):
        if (kbd.is_pressed('ctrl+shift+z')):
            sleep(0.3)
            gui.hotkey('ctrl','c')
            print('Order detail:'+pyperclip.paste().replace('\n',''))
            new_tab()
            paste('https://sellercentral.amazon.com/orders-v3/order/' + pyperclip.paste())
            gui.press('enter')
            sleep(0.1)
            gui.hotkey('alt','tab')
        elif (kbd.is_pressed('ctrl+shift+x')):
            sleep(0.3)
            gui.hotkey('ctrl','c')
            print('Removal detail:'+pyperclip.paste().replace('\n',''))
            new_tab()
            asin = pyperclip.paste().replace('+','%2B').replace('/','%2F')
            paste('https://sellercentral.amazon.com/recoveryui/removal-order/detail?sourceRemovalOrderId=' + pyperclip.paste())
            gui.press('enter')
        elif (kbd.is_pressed('ctrl+shift+s')):
            sleep(0.3)
            gui.hotkey('ctrl','c')
            print('Contact customer:'+pyperclip.paste().replace('\n',''))
            new_tab()
            paste('https://sellercentral.amazon.com/messaging/contact?orderID=' + pyperclip.paste() + '&marketplaceID=')
            if pyperclip.paste()[0]=='1':
                paste('ATVPDKIKX0DER')
            elif pyperclip.paste()[0]=='7':
                paste('A2EUQ1WTGCTBG2')
            #A2EUQ1WTGCTBG2 for canada market
            #ATVPDKIKX0DER for US market
            gui.press('enter')
        elif (kbd.is_pressed('ctrl+shift+d')):
            sleep(0.3)
            print('Email customer:'+pyperclip.paste())
            paste(email[0]+pyperclip.paste()+email[1])
    sleep(0.05)