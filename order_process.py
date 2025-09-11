import openpyxl as pxl
import datetime
from tkinter import filedialog

purchaseDate = []
orderNumber = []


#od.self()
def format():
    filepath = filedialog.askopenfilename()
    file = open(filepath,'r',encoding='utf-8')
    lines = file.readlines()[1:-1]
    orders = []
    for line in lines:
        cells = []
        for cell in line.split('\t'):
            if cell != '':
                cells.append(cell)
        orders.append(cells)
    orders.reverse()    
    return orders

wb = pxl.Workbook()
ws = wb['Sheet']
row = 1
for column in format():
    if column[11] == 'Cancelled':
        continue
    date = column[2][0:10].split('-')
    ws.cell(row,1,datetime.datetime(int(date[0]),int(date[1]),int(date[2]))).number_format = "yyyy/mm/dd" #date
    ws.cell(row,3,column[1]) #order-number
    ws.cell(row,5,column[10]) #asin
    ws.cell(row,6,int(column[12])) #quantity
    ws.cell(row,7,column[11]) #order-state

    row+=1
wb.save(filedialog.asksaveasfilename(filetypes=[('Excel','*.xlsx'), ("All files", "*.*")]))