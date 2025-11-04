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
    if pyperclip.paste().replace('\n','').replace('\t','').replace('\r','')=='':
        return 0
    gui.click(gui.locateOnScreen('img/ziniaologo.png',confidence=0.900))
    gui.hotkey('ctrl','0')
    print('Order detail:'+pyperclip.paste().replace('\n',''))
    gui.hotkey('ctrl','t')
    gui.press('tab',3)
    pyperclip.copy('https://sellercentral.amazon.com/orders-v3/order/' + pyperclip.paste())
    gui.hotkey('ctrl','v')
    gui.press('enter')

    #等待页面加载
    while (1):
            try:
                gui.moveTo(gui.locateOnScreen('img/order_finished.png',confidence=0.900))
                sleep(0.5)
                while 1:
                    try:
                        date = gui.locateOnScreen('img/deliverdate.png',confidence=0.800)
                        gui.moveTo(date.left+date.width,date.top+date.height)
                        gui.dragTo(date.left+date.width+230,date.top+date.height,0.2)
                        gui.hotkey('ctrl','c')
                        gui.hotkey('alt','tab')
                        gui.press('left')
                        date = pyperclip.paste().replace('\n','').replace('\t','')
                        year = date[0:4]
                        month = date[5:].split('月')[0]
                        day = date[5:].split('月')[1].split('日')[0]
                        print(month)
                        pyperclip.copy(year+'/'+month+'/'+day)
                        gui.hotkey('ctrl','v')
                        gui.press('right')
                        gui.hotkey('alt','tab')
                        break
                    except:
                        continue
                gui.keyDown('shift')
                gui.scroll(-400)
                gui.keyUp('shift')
                while 1:
                    try:
                        gui.locateOnScreen('img/refund.png',confidence=0.800)
                        print('Refund found, skiping...')
                        gui.hotkey('alt','tab')
                        gui.press('enter')
                        return 1
                    except:
                        for i in range(0,3):
                            try:

                                gui.locateOnScreen('img/exchange.png',confidence=0.800)
                                print('Item replacement found, skiping...')
                                gui.hotkey('alt','tab')
                                gui.press('tab',4)
                                pyperclip.copy('换货')
                                gui.hotkey('ctrl','v')
                                gui.press('enter')
                                return 1
                            except:
                                print('replacement not found,'+str(i)+'/3')
                                continue
                        try:
                            gui.locateOnScreen('img/no_refund.png',confidence=0.800)
                            break
                        except:
                            continue
                while 1:
                    try:
                        buyer = gui.center(gui.locateOnScreen('img/contact_buyer.png',confidence=0.900))
                        break
                    except:
                        continue
                old_clip = pyperclip.paste().replace('\t','').replace('\n','')
                gui.moveTo(buyer.x+30,buyer.y)
                gui.dragTo(buyer.x+170,buyer.y,0.3)
                pyperclip.copy('')
                gui.hotkey('ctrl','c')
                break
            except:
                try:
                    gui.locateOnScreen('img/order_await.png',confidence=0.900)
                    pyperclip.copy('')
                    break
                except:
                    continue
    gui.hotkey('ctrl','w')

    gui.hotkey('alt','tab')
    gui.press('tab')
    if pyperclip.paste().replace('\t','').replace('\n','')!='':
        pyperclip.copy(pyperclip.paste().replace('\t','').replace('\n',''))
        gui.hotkey('ctrl','v')
        gui.press('tab',3)
        pyperclip.copy('付款完成')
    elif pyperclip.paste().replace('\t','').replace('\n','')=='':
        gui.press('tab',3)
        pyperclip.copy('等待中')
    gui.hotkey('ctrl','v')
    gui.press('enter')

def email_user():
    gui.hotkey('ctrl','c')
    order_number = pyperclip.paste().replace('\t','').replace('\n','').replace('\r','')
    gui.click(gui.locateOnScreen('img/ziniaologo.png',confidence=0.900))

    #See if contacted customer previously
    gui.hotkey('ctrl','t')
    gui.press('tab',3)
    pyperclip.copy('https://sellercentral.amazon.com/messaging/inbox?&fi=search&ss='+order_number)
    gui.hotkey('ctrl','v')
    gui.press('enter')
    while 1:
        try:
            gui.click(gui.locateOnScreen('img/fold_message.png',confidence=0.900))
            break
        except:
            continue
    while 1:
        try:
            gui.locateOnScreen('img/message_sent.png',confidence=0.900)
            gui.hotkey('ctrl','w')
            gui.hotkey('alt','tab')
            gui.press('tab',5)
            pyperclip.copy('曾联系')
            gui.hotkey('ctrl','v')
            gui.press('enter')
            return 1
        except:
            try:
                gui.locateOnScreen('img/no_message.png',confidence=0.900)
                gui.hotkey('ctrl','w')
                break
            except:
                continue

    print('Order detail:'+order_number)
    gui.hotkey('ctrl','t')
    gui.press('tab',3)
    site = 'https://sellercentral.amazon.com/messaging/contact?orderID='+order_number+'&marketplaceID='
    if order_number[0]=='1':
        site+='ATVPDKIKX0DER'
    elif order_number[0]=='7':
        site+='A2EUQ1WTGCTBG2'
    pyperclip.copy(site)
    gui.hotkey('ctrl','v')
    gui.press('enter')
    gui.hotkey('ctrl','0')

    while (1):
        sleep(1)
        try:
            location = gui.locateOnScreen('img/reachable.png',confidence=0.900)
            print('found reachable')
            gui.click(location.left+10,location.top+10)
            while (1):
                try:
                    name_start = gui.locateOnScreen('img/name_start.png',confidence=0.900)
                    print('found name_start')
                    name_end = gui.locateOnScreen('img/name_end.png',confidence=0.900)
                    print('found name_end')
                    gui.moveTo(name_start.left+name_start.width,name_start.top+name_start.height/2)
                    gui.dragTo(name_end.left+10,name_end.top+name_end.height/2,0.5)
                    gui.hotkey('ctrl','c')
                    name = pyperclip.paste().capitalize()
                    break
                except:
                    continue
            while (1):
                try:
                    lang = gui.locateOnScreen('img/lang_en.png',confidence=0.900)
                    print('English')
                    gui.click(lang.left,lang.top+150)
                    pyperclip.copy(en_mail[0]+name+en_mail[1])
                    gui.hotkey('ctrl','v')
                    break
                except:
                    try:
                        lang = gui.locateOnScreen('img/lang_fr.png',confidence=0.900)
                        print('French')
                        gui.click(lang.left,lang.top+150)
                        pyperclip.copy(fr_mail[0]+name+fr_mail[1])
                        gui.hotkey('ctrl','v')
                        break
                    except:
                        try:
                            lang = gui.locateOnScreen('img/lang_sp.png',confidence=0.900)
                            print('Spanish')
                            gui.click(lang.left,lang.top+150)
                            pyperclip.copy(sp_mail[0]+name+sp_mail[1])
                            gui.hotkey('ctrl','v')
                            break
                        except:
                            continue
            gui.moveTo(lang.left,lang.top)
            sleep(1)
            gui.scroll(-1000)
            gui.scroll(-1000)
            sleep(0.1)
            while(1):
                try:
                    send = gui.locateOnScreen('img/send.png',confidence=0.900)
                    gui.click(send.left+100,send.top+30)
                    print('Ready to send, press \"ctrl+c\" to exit.')
                    break
                except:
                    continue
            '''
            while(1):
                try:
                    gui.click(gui.locateOnScreen('img/send_2.png',confidence=0.900))
                    break
                except:
                    continue
            '''
            while 1:
                if kbd.is_pressed('enter') == 1:
                    sleep(0.5)
                    try:
                        send = gui.locateOnScreen('img/send_final.png',confidence=0.900)
                        gui.click(send.left-100,send.top+100)
                        break
                    except:
                        continue
                if kbd.is_pressed('ctrl+c') == 1:
                    sleep(0.5)
                    return 0
            while(1):
                try:
                    gui.locateOnScreen('img/sent_status.png',confidence=0.900)
                    break
                except:
                    if (kbd.is_pressed('ctrl+c')):
                        return 0
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
                location = gui.locateOnScreen('img/no_reach.png',confidence=0.900)
                gui.hotkey('ctrl','w')
                gui.hotkey('alt','tab')
                gui.press('tab',5)
                pyperclip.copy('无法联系')
                gui.hotkey('ctrl','v')
                sleep(0.2)
                gui.press('enter')
                break
            except:
                continue
    
print('ctrl+shift+s: collect user name\nctrl+shift+d: send user email\nctrl+c: exit')
while(1):
    if (kbd.is_pressed('ctrl+shift+d')):
        sleep(1)
        while(1):
            if email_user()==0:
                print('ctrl+shift+s: collect user name\nctrl+shift+d: send user email\nctrl+c: exit')
                break
    elif (kbd.is_pressed('ctrl+shift+s')):
        sleep(1)
        while (1):
            if get_user_name()==0:
                print('ctrl+shift+s: collect user name\nctrl+shift+d: send user email\nctrl+c: exit')
                break
    elif (kbd.is_pressed('ctrl+c')):
        exit()
    sleep(0.1)
