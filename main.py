# Interface simples

from conversor import cel_fah
from conversor import fah_cel

while True:
    # Apresentação
    print('\n\t\t\t -- Conversor --\n')

    # Menu
    print('1. Converter ºC em ºF')
    print('2. Converter ºF em ºC')
    print('3. Sair')

    # Ler a opção do usuário
    op = int(input('\nInforme a opção: '))

    if op == 1:
        # Entrada
        cel = float(input('Informe a temperatura em ºC: '))

        # Processamento
        fah = cel_fah(cel)

        # Saída
        print('\n{:.2f}ºC = {:.2f}ºF\n'.format(cel, fah))
    elif op == 2:
        fah = float(input('Informe a temperatura em Fº:'))
         
        #Processamento
        cel = fah_cel(fah)

        #Saida 
        print('\n{:.2f}ºF = {:.2f}ºC\n'.format(fah, cel))
    elif op == 3:
        print('Forte abraço!')
        break
    else:
        print('Opcão inavalida! Tente novamente.')
