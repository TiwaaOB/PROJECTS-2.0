# NAME: OPOKU-BOATENG TIWAA ABENA
# ID: 10974363
# DEPARTMENT: BMEN

import qrcode
import PySimpleGUI as sg


qrc_image=[sg.Image('',key='-QRCODE-',size=(350,350),background_color='black')]

layout=[
    [sg.Text('Enter URL: ')],
    [sg.Input('',key='-URL-',justification='center')],
    [sg.Button('Create',key='-submit-',expand_x=True,button_color='red')],
    [sg.Column([qrc_image],justification='center')],
]

wind = sg.Window('QRCODE Generator App',layout)

while True:
    event,values = wind.read()
    if event==sg.WIN_CLOSED:
        break
    elif event == '-submit-':
        url = values['-URL-']
        if url:
            image= qrcode.make(url)
            image.save('qr.png')
            wind['-QRCODE-'].update('qr.png')
wind.close()
