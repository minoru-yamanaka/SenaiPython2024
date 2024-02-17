import random
import time

vitorias = 0
derrotas = 0

while True:
    print('Escolha uma opção:')
    time.sleep(0.2)
    print('(P) --> Par')
    time.sleep(0.2)
    print('(I) --> Impar')
    time.sleep(0.2)
    print('(X) --> Finalizar')
    time.sleep(0.2)

    escolha = input('Opção: ').upper()

    if escolha not in ('P', 'I', 'X'):
        print('Escolha inválida, tente novamente\n')
        time.sleep(1)
        continue
    elif escolha == 'X':
        print('Finalizando o programa')
        time.sleep(1)
        break

    num_jogador = int(input('Digite um número de 1 a 10: '))

    if num_jogador < 1 or num_jogador > 10:
        time.sleep(1)
        print('Escolha inválida, tente novamente')
        continue

    num_pc = random.randint(1, 10)

    soma = num_jogador + num_pc

    time.sleep(1)
    print('O PC escolheu ' + str(num_pc))
    time.sleep(1)
    print('A soma é ' + str(soma))
    time.sleep(1)

    print('Analisando resultado', end='')
    for i in range(3):
        time.sleep(0.5)
        print('.', end='')
    print('\n')
    time.sleep(1)

    if escolha == 'P':
        if soma % 2 == 0:
            print('Você venceu')
            vitorias += 1
        else:
            print('Você perdeu')
            derrotas += 1
    elif escolha == 'I':
        if soma % 2 == 0:
            print('Você perdeu')
            derrotas += 1
        else:
            print('Você venceu')
            vitorias += 1

    time.sleep(1)
    print('\n' + '*' * 40)
    time.sleep(0.2)
    print('Vitórias: ' + str(vitorias))
    time.sleep(0.2)
    print('Derrotas: ' + str(derrotas))
    time.sleep(0.2)
    print('*' * 40 + '\n')
    time.sleep(1)