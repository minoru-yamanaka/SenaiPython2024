# 1)Faça um programa que peça um número ao usuário e informe se é Par ou Ímpar.
class ParouImpar:
    def __init__(self):
        num = float(input('Insira um número: '))
        resultado = num % 2

        if resultado == 0:
            print('Este número é Par ')
        else :
            print('Este número é Ímpar ')

call_ParouImpar = ParouImpar()