# 1)	Faça um programa para adivinhar um número de 1 a 10000.
# Se você errar o computador deverá responder se é mais ou menos.
# Se você errar 10 vezes você perde o jogo

import random


class adivinharNumero:
    def __init__(self):

        tent = 0
        numeroGerado = random.randint(1, 10000)
        print('''-- Jogo da Adivinhação --''')

        while tent < 10:
            print('Tentativa:  ' + str(tent))
            chuteUsuario = int(input('Tente adivinhar o número escolhido pelo pc: '))

            if chuteUsuario == numeroGerado:
                print('Parabéns! Você adivinhou o número. O número é: ' + str(numeroGerado))
                break
            elif chuteUsuario < numeroGerado:
                tent += 1
                print('O número é maior.')
            else:
                tent += 1
                print('O número é menor.')
        else:
            print('Você errou o máximo de vezes. O número é: ' + str(numeroGerado))
call_adivinharNumero = adivinharNumero()