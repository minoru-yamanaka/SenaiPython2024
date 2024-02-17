
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

JogadorVida = 10
ComputadorVida = 10

rodadas = 0

while JogadorVida > 0 and ComputadorVida > 0:
    rodadas = rodadas + 1
    print('Rodada ' + str(rodadas))
    print('Vida do Jogador: ' + str(JogadorVida) + ' | Vida do Computador: ' + str(ComputadorVida))

    escolha = int(input('''Escolha seu ataque 
    ( 1 ) Cabeçada  
    ( 2 ) Soco 
    '''))

    if escolha == 1:
        # cabeçada
        JogadorVida -= 3
        ComputadorVida -= 1
        print('Você desferiu uma Cabeçada!')
    elif escolha == 2:
        # soco
        poder_ataque_jogador = random.randint(1, 6)
        poder_ataque_computador = random.randint(1, 6)

        if poder_ataque_jogador > poder_ataque_computador:
            ComputadorVida -= poder_ataque_jogador
            print('Você desferiu um Soco com poder ' + str(poder_ataque_jogador))
        elif poder_ataque_jogador == poder_ataque_computador:
            print('Empate! Nenhum dano foi causado.')
        else:
            JogadorVida -= poder_ataque_computador
            print('Você desferiu um Soco com poder ' + str(poder_ataque_jogador) + ', mas o computador contra-atacou!')
    else:
        print('Escolha inválida. Por favor, escolha entre Cabeçada ou Soco.')
        continue
    rodadas += 1

if JogadorVida <= 0:
    print('Você perdeu! O computador venceu.')
elif ComputadorVida <= 0:
    print('Parabéns! Você venceu o computador!')

print('Total de rodadas jogadas: ' + str(rodadas))
