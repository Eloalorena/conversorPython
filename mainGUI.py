# Interface gráfica do conversor de temperatura
import PySimpleGUI as psg

import conversor

frame_layout = [
    [psg.Radio('Celsius -> Fahrenheit', 'GRUPO2', default=True, key='cel_fah', enable_events=True)], # Erro3
    [psg.Radio('Fahrenheit -> Celsius', 'GRUPO1', key='fah_cel', enable_events=True)] # Erro4
]
layout = [
    [psg.Text('Informe a temperatura em ºC: ', key='rotulo'), psg.InputText(key='temp'), psg.Frame('Opções: ', layout=frame_layout)],
    [psg.Text('', key='resultado')],
    [psg.Button('Converter'), psg.Button('Limpar')],
]

janela = psg.Window('Conversor', layout)
'   '
while True:
    evento, valor = janela.read()

    if evento == psg.WIN_CLOSED or evento == 'Exit':
        break
    
    elif valor.get('cel_fah' , False): # Atualiza o rotulo
        janela['rotulo'].update('Informe a temperatura em ºC: ')
    
    elif valor.get ('fah_cel', False):
        janela['rotulo'].update('Informe a temperatura em ºF: ')

    elif evento == 'Limpar':
        janela['temp'].update('')
        janela['temp'].set_focus() 
        janela['resultado'].update('')
    elif evento == 'Converter':
        try:
            temp = float(valor['temp'])
            if valor['cel_fah']:
                fah = conversor.cel_fah(temp)
                janela['resultado'].update('{:.2f} ºF'.format(fah))
            else:
                cel = conversor.fah_cel(temp)
                janela['resultado'].update('{:.2f} ºC'.format(cel))
        except Exception as e:
            janela['resultado'].update('Valor inválido!')
            
janela.close()
