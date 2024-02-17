# 4)    Faça um jogo de batalha entre você e o computador:
#    - Cada um dos jogadores inicia com 10 pontos de vida.
#    - Neste jogo, você deverá comparar o poder de combate em cada turno;
#    quem ganhar desfere o ataque no oponente causando o dano respectivo.
#    - Você tem dois ataques, que poderá selecionar no início de cada rodada:
#      1. **Cabeçada**: Tem poder de combate 4, se ganhar tira 3 de vida do oponente e toma 1 de dano.
#      2. **Soco**: Tem poder de combate aleatório (jogar no dado D6) e, caso ganhe, causa dano aleatório (jogar no dado D6).
#    - O computador tem apenas o ataque Soco.
#    - Quem chegar a 0 pontos de vida perde o jogo.

titulo = 'Jogo de Luta'
'''
Data: 04/10/2023
Autor: Daniel
Descrição: Jogo de luta entre usuário e PC
'''
print('Bem vindo ao programa ' + titulo)

import random
import time

vida_jog = 10
vida_PC = 10

print('Bem vindo ao Jogo de Luta')
time.sleep(1)
while True:
    print('''Escolha uma opção:
(S) --> Soco
(C) --> Cabeçada
(I) --> Informações''')
    escolha = input('Opção: ').upper()

    if escolha not in ('S','C','I'):
        print('Opção inválida')
        time.sleep(1)
        continue
    elif escolha == 'I':
        time.sleep(0.5)
        print('\nAtaques:')
        time.sleep(0.3)
        print('\tSoco:')
        time.sleep(0.3)
        print('\t\tPoder de Combate: ',end='')
        time.sleep(0.3)
        print('Dado de 1 a 6')
        time.sleep(0.3)
        print('\t\tDano: ', end='')
        time.sleep(0.3)
        print('Dado de 1 a 6')
        time.sleep(0.3)

        print('\tCabeçada:')
        time.sleep(0.3)
        print('\t\tPoder de Combate: ', end='')
        time.sleep(0.3)
        print('4')
        time.sleep(0.3)
        print('\t\tDano: ', end='')
        time.sleep(0.3)
        print('3')
        time.sleep(0.3)
        print('\t\tDano Recebido: ', end='')
        time.sleep(0.3)
        print('1')
        time.sleep(1)
        continue
    time.sleep(1)
    if escolha == 'S':
        print('Você irá atacar com Soco')
        combate_jog = random.randint(1, 6)
        dano_jog = random.randint(1, 6)
        dano_recebido_jog = 0
    elif escolha == 'C':
        print('Você irá atacar com Cabeçada')
        combate_jog = 4
        dano_jog = 3
        dano_recebido_jog = 1

    combate_PC = random.randint(1,6)
    dano_PC = random.randint(1,6)

    print('Seu poder de combate é ', end='')
    for i in range(3):
        time.sleep(0.3)
        print('.', end=' ')
    print(combate_jog)

    time.sleep(1)

    print('O poder de combate do PC é ', end='')
    for i in range(3):
        time.sleep(0.3)
        print('.', end=' ')
    print(combate_PC)

    print('Verificando resultado ', end='')
    for i in range(3):
        time.sleep(0.3)
        print('.', end=' ')
    print()
    time.sleep(2)

    if combate_jog > combate_PC:
        print('Você ganhou o turno')
        time.sleep(1)
        print('Você desferiu ' + str(dano_jog) + ' de dano')
        vida_PC -= dano_jog
        if dano_recebido_jog > 0:
            time.sleep(1)
            print('Você tomou ' + str(dano_recebido_jog) + ' de dano')
            vida_jog -= dano_recebido_jog
    elif combate_jog < combate_PC:
        print('Você perdeu o turno')
        time.sleep(1)
        print('O PC desferiu ' + str(dano_PC) + ' de dano')
        vida_jog -= dano_PC
    else:
        print('O turno Empatou')

    time.sleep(2)

    print('\n' + '*' * 40)
    time.sleep(0.3)
    print('Vida Jogador: ' + str(vida_jog))
    time.sleep(0.3)
    print('Vida PC: ' + str(vida_PC))
    time.sleep(0.3)
    print('*' * 40 + '\n\n')
    time.sleep(1)

    if vida_jog <= 0:
        print('Você perdeu')
        time.sleep(1)
        break
    elif vida_PC <= 0:
        print('Você ganhou')
        time.sleep(1)
        break


