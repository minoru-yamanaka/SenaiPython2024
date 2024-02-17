# 4)    Faça um jogo de batalha entre você e o computador:
#    - Cada um dos jogadores inicia com 10 pontos de vida.
#    - Neste jogo, você deverá comparar o poder de combate em cada turno;
#    quem ganhar desfere o ataque no oponente causando o dano respectivo.
#    - Você tem dois ataques, que poderá selecionar no início de cada rodada:
#      1. **Cabeçada**: Tem poder de combate 4, se ganhar tira 3 de vida do oponente e toma 1 de dano.
#      2. **Soco**: Tem poder de combate aleatório (jogar no dado D6) e, caso ganhe, causa dano aleatório (jogar no dado D6).
#    - O computador tem apenas o ataque Soco.
#    - Quem chegar a 0 pontos de vida perde o jogo.

import random
from time import sleep

num_vit = 0
num_emp = 0
num_der = 0

while True:
    print('Escolha uma opção:')
    sleep(0.2)
    print('(R) --> Pedra')
    sleep(0.2)
    print('(P) --> Papel')
    sleep(0.2)
    print('(T) --> Tesoura')
    sleep(0.2)
    print('(X) --> Sair')
    sleep(0.2)
    escolha_jogador = input('Opção: ').upper()

    if escolha_jogador not in ('R', 'P', 'T', 'X'):
        print('Escolha inválida')
        sleep(1)
        continue
    elif escolha_jogador == 'X':
        print('Finalizando o programa')
        sleep(1)
        break

    escolha_pc = random.randint(1, 3)
    if escolha_pc == 1:
        escolha_pc = 'R'
    elif escolha_pc == 2:
        escolha_pc = 'P'
    else:
        escolha_pc = 'T'

    sleep(1)
    print('Você escolheu ... ', end='')
    sleep(1)
    if escolha_jogador == 'R':
        print('Pedra')
    elif escolha_jogador == 'P':
        print('Papel')
    else:
        print('Tesoura')

    sleep(1)
    print('O PC escolheu ... ', end='')
    sleep(1)
    if escolha_pc == 'R':
        print('Pedra')
    elif escolha_pc == 'P':
        print('Papel')
    else:
        print('Tesoura')
    sleep(1)
    print('Analisando Resultado...')
    sleep(2)

    if escolha_jogador == 'R' and escolha_pc == 'P':
        print('Você perdeu!')
        sleep(1)
        print('Papel embrulha Pedra')
        num_der += 1
    elif escolha_jogador == 'R' and escolha_pc == 'T':
        print('Você venceu!')
        sleep(1)
        print('Pedra quebra Tesoura')
        num_vit += 1
    elif escolha_jogador == 'P' and escolha_pc == 'R':
        print('Você venceu!')
        sleep(1)
        print('Papel embrulha Pedra')
        num_vit += 1
    elif escolha_jogador == 'P' and escolha_pc == 'T':
        print('Você perdeu!')
        sleep(1)
        print('Tesoura corta Papel')
        num_der += 1
    elif escolha_jogador == 'T' and escolha_pc == 'R':
        print('Você perdeu!')
        sleep(1)
        print('Pedra quebra Tesoura')
        num_der += 1
    elif escolha_jogador == 'T' and escolha_pc == 'P':
        print('Você venceu!')
        sleep(1)
        print('Tesoura corta Papel')
        num_vit += 1
    else:
        print('Empatou!')
        num_emp += 1

    sleep(1)
    print('\n' + '*' * 40)
    sleep(0.2)
    print('Vitórias: ' + str(num_vit))
    sleep(0.2)
    print('Empate: ' + str(num_emp))
    sleep(0.2)
    print('Derrotas: ' + str(num_der))
    sleep(0.2)
    print('*' * 40 + '\n')
    sleep(2)