import py

sg.theme('Dark')

layout = [[sg.Text('Oiii'), sg.InputText()],
          [sg.Button('Saii, saii TIRA'), sg.Button('Oii linda!')]]


janela = sg.Window('Coisa', layout)


while True:
    event, value = janela.read()
    if event == sg.WIN_CLOSED:
        print('Tu fechou a janela')
        break
    elif event == 'Saii, saii TIRA':
        print('É o zoiooo memo caraiooooo')
        print(value[0])
    else:
        print('É muié')
        if value[0] == '':
            sg.theme('BrownBlue')
            sg.Popup('Digita algo prfv')

janela.close()




