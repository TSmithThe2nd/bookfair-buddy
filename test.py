import PySimpleGUI as sg
import pandas as pd
# import openpyxl as pyxl
# from openpyxly import Workbook
# from openpyxl.worksheet.table import Table, TableStyleInfo
sg.theme('lightgreen')

# wb=Workbook()
# ws=wb.active

EXCEL_FILE= "bookfairbuddy.xlsx"

df=pd.read_excel(EXCEL_FILE)

# create form structure

# layouts
student=[[sg.Text('First Name'),sg.Input(key='Firt Name')],
         [sg.Text('Last Name'),sg.Input(key='Last Name')],
         [sg.Text('Teacher'),sg.Input(key='Teacher Name')],
         [sg.Text('Book Name'),sg.Input(key='Book Name')],
         [sg.Text('Price'),sg.Input(key='Price')],
         [sg.Combo(['Kindergarden','1st','2nd','3rd','4th','5th','6th'], default_value='Kindergarden', key='Grade')],
          [sg.Button('Submit Book'), sg.Button('Clear All'), sg.Exit()]
         ]

Shelf=[[sg.Text('Book Name'),sg.Input(key='Book Name')],
       [sg.Text('Price'),sg.Input(key='Price')],
       [sg.Text('Number to Order'),sg.Input(key='Number to Order')],
        [sg.Submit(), sg.Button('Clear'), sg.Exit()]

         ]

# tab groups
tabs=[[sg.TabGroup([[sg.Tab('Student', student),
                    sg.Tab('Shelf', Shelf)]])]]
#launch window
window=sg.Window("Testing simple gui", tabs)

#test table format
def clear_input():
    for key in values:
        window[key]('')
    return None

#logic
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Clear':
        clear_input()
    if event == 'Submit':
        df = df.append(values, ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        sg.popup('Data saved!')
        clear_input()
window.close()
