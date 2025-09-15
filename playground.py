import openpyxl as pxl
import tkinter as tk
from tkinter import filedialog
import pyautogui as gui
from time import sleep
import pyperclip
import keyboard as kbd

en_mail = [
'Subject: OUTOHOME Order Confirmation & Support Commitment\n\n\
Dear ',
',\n\n\
Thank you for purchasing OUTOHOME products on Amazon.\n\n\
We stand by our product quality and your satisfaction. Should any issues arise during product usage, contact us directly via Amazon Messages. Our support team will provide prompt assistance within 24 hours.\n\n\
We value your trust in OUTOHOME.\n\n\
Sincerely,\n\
OUTOHOME Team'
]

fr_mail = [
'Objet : Confirmation de votre commande OUTOHOME & Engagement à vos côtés\n\n\
Chère ',
',\n\n\
Merci d\'avoir choisi les produits OUTOHOME sur Amazon.\n\n\
Nous tenons à vous assurer de la qualité de nos produits et de votre entière satisfaction. Si jamais vous rencontrez un souci lors de l\'utilisation, n\'hésitez pas à nous contacter directement via les messages Amazon. Notre équipe d\'assistance vous répondra avec plaisir dans les 24 heures.\n\n\
Nous vous remercions pour la confiance que vous accordez à OUTOHOME.\n\n\
Avec toute notre considération,\n\
L\'équipe OUTOHOME'
]

sp_mail = [
'Asunto: Confirmación de su pedido OUTOHOME y compromiso de soporte\n\n\
Estimado ',
',\n\n\
Gracias por haber adquirido productos OUTOHOME en Amazon.\n\n\
Respaldamos la calidad de nuestros productos y su satisfacción. Si llegara a surgir algún problema durante el uso, por favor contáctenos directamente a través de los mensajes de Amazon. Nuestro equipo de soporte estará encantado de ayudarle y le dará respuesta en un plazo máximo de 24 horas.\n\n\
Valoramos mucho la confianza que deposita en OUTOHOME.\n\n\
Atentamente,\n\
El equipo de OUTOHOME'
]

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
    order_number = pyperclip.paste()
    gui.hotkey('ctrl','c')
    gui.click(gui.locateOnScreen('img/ziniaologo.png',confidence=0.800))
    gui.hotkey('ctrl','0')
    print('Order detail:'+pyperclip.paste().replace('\t','').replace('\n',''))
    gui.hotkey('ctrl','t')
    gui.press('tab',3)
    site = 'https://sellercentral.amazon.com/messaging/contact?orderID='+pyperclip.paste().replace('\t','').replace('\n','')
    site += '&marketplaceID='
    if pyperclip.paste()[0]=='1':
        site+='ATVPDKIKX0DER'
    elif pyperclip.paste()[0]=='7':
        site+='A2EUQ1WTGCTBG2'
    gui.write(site)
    gui.press('enter')
    while (1):
        try:
            location = gui.locateOnScreen('img/reachable.png',confidence=0.999)
            print('found reachable')
            gui.click(location.left+10,location.top+10)
            while (1):
                try:
                    name_start = gui.locateOnScreen('img/name_start.png',confidence=0.900)
                    print('found name_start')
                    name_end = gui.locateOnScreen('img/name_end.png',confidence=0.900)
                    print('found name_end')
                    gui.moveTo(name_start.left+name_start.width,name_start.top+name_start.height/2)
                    gui.dragTo(name_end.left+30,name_end.top+name_end.height/2,0.5)
                    gui.hotkey('ctrl','c')
                    name = pyperclip.paste()
                    break
                except:
                    continue
            while (1):
                try:
                    lang = gui.locateOnScreen('img/lang_en.png',confidence=0.800)
                    gui.click(lang.left,lang.top+100)
                    pyperclip.copy(en_mail[0]+name+en_mail[1])
                    gui.hotkey('ctrl','v')
                    break
                except:
                    try:
                        lang = gui.locateOnScreen('img/lang_fr.png',confidence=0.800)
                        gui.click(lang.left,lang.top+100)
                        pyperclip.copy(fr_mail[0]+name+fr_mail[1])
                        gui.hotkey('ctrl','v')
                        break
                    except:
                        try:
                            lang = gui.locateOnScreen('img/lang_sp.png',confidence=0.800)
                            break
                        except:
                            continue
            gui.move(0,200)
            sleep(1)
            gui.scroll(-1200)
            while(1):
                try:
                    gui.click(gui.locateOnScreen('img/send.png',confidence=0.800))
                    break
                except:
                    continue
            '''
            while(1):
                try:
                    gui.click(gui.locateOnScreen('img/send_2.png',confidence=0.800))
                    break
                except:
                    continue
            '''
            while(1):
                try:
                    gui.locateOnScreen('img/sent_status.png',confidence=0.800)
                    break
                except:
                    continue
            gui.hotkey('ctrl','w')
            gui.hotkey('alt','tab')
            gui.press('tab',5)
            pyperclip.copy('已发送')
            gui.hotkey('ctrl','v')
            gui.press('enter')
            break
        except:
            try:
                location = gui.locateOnScreen('img/no_reach.png',confidence=0.999)
                gui.hotkey('ctrl','w')
                gui.hotkey('alt','tab')
                gui.press('tab',5)
                pyperclip.copy('无法联系')
                gui.hotkey('ctrl','v')
                sleep(0.2)
                gui.press('enter')
                break
            except:
                print('')
    
    
while (kbd.is_pressed('ctrl+shift+s')!=1):
    sleep(0.1)
sleep(1)
while(1):
    email_user()
'''
while (1):
        get_user_name()
'''
