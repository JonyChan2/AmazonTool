import openpyxl as pxl
import tkinter as tk

def submit():
    print(order.get())
    wb = pxl.load_workbook('sample.xlsx')
    # Iterate through all sheets
    for sheet in wb.sheetnames:
        ws = wb[sheet]
        print(f"Searching in sheet: {sheet}")
        # Iterate through rows and columns
        for row in ws.iter_rows(values_only=True):
            print('searching: '+str(row))
            for cell in row:
                print('searching: '+str(cell))
                if str(cell) == order.get(): # Replace with your search term
                    print(f"Found '{cell}' in sheet '{sheet}'")
                    break

window = tk.Tk()
window.title('Test')
window.geometry('200x200')

order = tk.StringVar()
order.set('')

text = tk.Label(window,text='Last order number:',anchor='w').pack()
last_order = tk.Entry(window,textvariable=order).pack()
submit_btn = tk.Button(window,text='Submit',command=submit).pack()
window.mainloop()