# 2)Uma empresa de transporte público quer fazer um sistema automático para identificar se o usuário terá gratuidade
# no transporte ou não. Faça um programa que pergunte a idade do usuário, se ele tiver 65 anos ou mais irá informar que
# ele tem gratuidade no transporte.

class GratuidadeNoTransporte:
    def __init__(self):
        idade = int(input('Insira sua idade: '))

        if idade >= 65:
            print('Este o usuário tem gratuidade no transporte')
        else :
            print('Este o usuário não tem gratuidade no transporte')

call_GratuidadeNoTransporte = GratuidadeNoTransporte()