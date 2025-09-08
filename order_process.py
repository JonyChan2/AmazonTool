

#od.self()
def format():
    file = open('order.txt','r',encoding='utf-8')
    lines = file.readlines()[1:-1]
    orders = []
    for line in lines:
        cells = []
        for cell in line.split('\t'):
            if cell != '':
                cells.append(cell)
        orders.append(cells)
    return orders

