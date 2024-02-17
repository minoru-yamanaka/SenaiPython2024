
# 4) Faça um jogo de batalha entre você e o computador:
#    - Cada um dos jogadores inicia com 10 pontos de vida.
#    - Neste jogo, você deverá comparar o poder de combate em
# cada turno; quem ganhar desfere o ataque no oponente
# causando o dano respectivo.
#    - Você tem dois ataques, que poderá selecionar no início
#de cada rodada:
#      1. **Cabeçada**: Tem poder de combate 4, se ganhar
#tira 3 de vida do oponente e toma 1 de dano.
#      2. **Socorro**: Tem poder de combate aleatório (jogar
#no dado D6) e, caso ganhe, causa dano aleatório (jogar no dado D6).
#    - O computador tem apenas o ataque Soco.
#    - Quem chegar a 0 pontos de vida perde o jogo.

import random
class rpg:
    def __init__(self):
        # Contadores de vitórias, empates e derrotas

        Jogador = 10
        Computador = 10

        def run_rpg (self):
            while self.restart == 0:
                self.rodadas = int(input("::: RPG :::\nINSIRA A QUANTIDADE DE RODADAS: "))
                for i in range(1, self.rodadas + 1):
                    self.escolhaComputador = random.randint(1, 3)
                    self.rotuloEscolhaJogador()
                    self.escolhaJogador = int(input())
                    print("ESCOLHA DO COMPUTADOR:")
                    print(self.escolhaComputador)
                    self.verificaResultado()
                    self.exibePlacar()
                    self.restart += 1
                self.exibeResultado()
                self.restart = int(input("RESTART? [1]SIM ou [2]NÃO "))
            print("::: FIM DE JOGO :::")




# call_rpg = rpg()
