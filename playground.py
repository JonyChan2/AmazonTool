import pyautogui as gui
import pyperclip as ppc
import openpyxl as pxl

wb = pxl.load_workbook('sample.xlsx')
wb.active
ws = wb[wb.sheetnames[0]]
ws1 = ws['A1'].value
print(ws1)