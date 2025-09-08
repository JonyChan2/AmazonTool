import openpyxl as pxl
import tkinter as tk

def wb_search():
    print(order.get())
    # Iterate through all sheets
    for sheet in wb.sheetnames:
        ws = wb[sheet]
        # Iterate through rows and columns
        for row in ws.iter_rows(values_only=False):
            for cell in row:
                if str(cell.value) == order.get(): # Replace with your search term
                    print(f"Found '{cell.value}' in sheet '{sheet}', coordinate: {cell.coordinate}")
                    return 

def ws_index():
    ws_index = []
    for row in wb['Sheet'].iter_rows(values_only=0):
        ws_index.append(row)
    return ws_index

wb = pxl.load_workbook('sample.xlsx')

window = tk.Tk()
window.title('Order Processor')
window.geometry('200x200')

order = tk.StringVar()
order.set('')

text = tk.Label(window,text='Last order number:',anchor='w').pack()
last_order = tk.Entry(window,textvariable=order).pack()
submit_btn = tk.Button(window,text='Submit',command=wb_search).pack()
window.mainloop()