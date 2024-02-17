titulo = 'Adivinhe o número'
'''
Data: 04/05/2023
Autor: Daniel
Descrição: Jogo para adivinhar um número
de 1 a 10000
'''
print('Bem vindo ao programa ' + titulo)

import random

while True:
    print('''
    Dificuldade:
    1 --> Adivinhe um número de 1 a 100
    2 --> Adivinhe um número de 1 a 1000
    3 --> Adivinhe um número de 1 a 1500
    4 --> Adivinhe um número de 1 a 2000
    5 --> Adivinhe um número de 1 a 3000
    6 --> Adivinhe um número de 1 a 4000
    7 --> Adivinhe um número de 1 a 5000
    8 --> Adivinhe um número de 1 a 7000
    9 --> Adivinhe um número de 1 a 10000
    10 --> Adivinhe um número de 1 a 15000
    ''')
    escolha = input('Escolha a dificuldade: ')

    if escolha == '1':
        limite = 100
        break
    elif escolha == '2':
        limite = 1000
        break
    elif escolha == '3':
        limite = 1500
        break
    elif escolha == '4':
        limite = 2000
        break
    elif escolha == '5':
        limite = 3000
        break
    elif escolha == '6':
        limite = 4000
        break
    elif escolha == '7':
        limite = 5000
        break
    elif escolha == '8':
        limite = 7000
        break
    elif escolha == '9':
        limite = 10000
        break
    elif escolha == '10':
        limite = 15000
        break


numero_secreto = random.randint(1,limite)
print('Adivinhe o numero secreto entre 1 e ' + str(limite))
#print(numero_secreto)

melhor_chute = 100000

for tentativa in range(1,11):
    print('\n' + '#'*40)
    print('Tentativa: ' + str(tentativa))
    numero = int(input('Digite um número: '))

    if abs(numero_secreto - numero) < abs(numero_secreto - melhor_chute):
        melhor_chute = numero

    if numero_secreto == numero:
        print('Você acertou!!!')
        break
    elif tentativa < 10:
        if numero_secreto > numero:
            print('Digite um número maior')
        else:
            print('Digite um número menor')
else:
    print('\nVocê perdeu!!! O número era ' + str(numero_secreto))
    print('Sua melhor tentativa foi ' + str(melhor_chute))
    print('Você errou por ' + str(abs(numero_secreto - melhor_chute)))