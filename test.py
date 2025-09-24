import pyperclip

print(pyperclip.paste().replace('\n','').replace('\t','').replace('\r',''))
if pyperclip.paste().replace('\n','').replace('\t','').replace('\r','')=='':
    print('bingo')