import pyautogui as gui
from time import sleep
import pyperclip
import keyboard as kbd

def check():
    gui.hotkey('ctrl','c')
    gui.hotkey('alt','tab')
    gui.hotkey('ctrl','t')
    gui.press('tab',3)
    order = pyperclip.paste().replace('\n','').replace('\t','').replace('\r','')
    pyperclip.copy('https://sellercentral.amazon.com/orders-v3/order/'+order)
    gui.hotkey('ctrl','v')
    gui.press('enter')
    while 1:
        try:
            gui.moveTo(gui.locateOnScreen('img/order_finished.png',confidence=0.900))
            break
        except:
            try:
                gui.moveTo(gui.locateOnScreen('img/order_canceled.png',confidence=0.900))
                gui.hotkey('alt','tab')
                gui.press('tab')
                gui.write('canceled')
                gui.press('enter')
                return
            except:
                continue
    
    gui.keyDown('shift')
    gui.scroll(-400)
    gui.keyUp('shift')
    #sleep(1)
    while 1:
        try:
            gui.locateOnScreen('img/refund.png',confidence=0.900)
            gui.hotkey('ctrl','w')
            gui.hotkey('alt','tab')
            gui.press('tab',1)
            gui.write('refunded')
            break
        except:
            try:
                gui.locateOnScreen('img/no_refund.png',confidence=0.900)
                gui.hotkey('ctrl','w')
                gui.hotkey('alt','tab')
                gui.press('tab',1)
                gui.write('no_refund')
                break
            except:
                continue
    gui.press('enter')

def date_format():
    while 1:
        gui.hotkey('ctrl','c')
        if pyperclip.paste()=='':
            break
        pyperclip.copy(pyperclip.paste()[0:10].replace('-','/'))
        gui.hotkey('ctrl','v')
        gui.press('enter')
'''
while 1:
    if kbd.is_pressed('ctrl+shift+s'):
        break
    sleep(0.1)
sleep(1)
'''
while 1:
    while 1:
        try:
            gui.click(gui.locateOnScreen('img/ziniaologo.png',confidence=0.900))
            break
        except:
            continue
    gui.hotkey('ctrl','t')
    pyperclip.copy('https://sellercentral.amazon.com/reportcentral/CUSTOMER_RETURNS/1')
    gui.press('tab',3)
    gui.hotkey('ctrl','v')
    gui.press('enter')

    while 1:
        sleep(1)
        try:
            gui.click(gui.locateOnScreen('img/lastday.png',confidence=0.990))
            gui.press('down',5)
            gui.press('enter')
            print('Choose the period, then click ENTER.')
            break
        except:
            continue

    while 1:
        if kbd.is_pressed('enter')!=1:
            continue
        try:
            gui.click(gui.locateOnScreen('img/txt_download.png',confidence=0.900))
            break
        except:
            continue

    break
