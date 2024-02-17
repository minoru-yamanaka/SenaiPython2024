import random
import time

num_vit = 0
num_der = 0

# ciclo do jogo
while True:
    # Sistema de Escolhas
    print('''Escolha uma opção:
(P) --> Par
(I) --> Impar
(X) --> Sair''')
    escolha = input('Opção: ').upper()

    time.sleep(1)
    # Validação das escolhas
    if escolha not in ('P', 'I', 'X'):
        print('Opção inválida\n')
        time.sleep(1)
        continue
    elif escolha == 'X':
        print('Encerrando do programa')
        time.sleep(2)
        break

    # Solicitar número
    num_jog = int(input('Digite um número de 0 a 10: '))
    time.sleep(0.5)
    # Validar se o número é entre 0 a 10
    if num_jog < 0 or num_jog > 10:
        print('Número inválido, tente novamente\n')
        time.sleep(1)
        continue

    # Definir número do PC
    num_pc = random.randint(0, 10)

    # Somar os números
    soma = num_jog + num_pc

    # Imprimir valores do jogo
    time.sleep(1)
    print('Você jogou ' + str(num_jog))
    time.sleep(1)
    print('O PC jogou ' + str(num_pc))
    time.sleep(1)
    print('A Soma é ' + str(soma))
    time.sleep(1)
    print('Analisando resultado...')
    time.sleep(2)
    # Verificar quem ganhou
    if escolha == 'P' and soma % 2 == 0:
        print('Você ganhou')
        num_vit += 1
    elif escolha == 'P' and soma % 2 > 0:
        print('O PC ganhou')
        num_der += 1
    elif escolha == 'I' and soma % 2 == 0:
        print('O PC ganhou')
        num_der += 1
    elif escolha == 'I' and soma % 2 > 0:
        print('Você ganhou')
        num_vit += 1
    time.sleep(1)
    print('\n' + '*' * 40)
    time.sleep(0.3)
    print('Vitórias: ' + str(num_vit))
    time.sleep(0.3)
    print('Derrotas: ' + str(num_der))
    time.sleep(0.3)
    print('*' * 40 + '\n\n')

    time.sleep(1)