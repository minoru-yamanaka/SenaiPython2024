
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

        Jogador = 10
        Computador = 10

        self.OPCOES = {
            "C": "Cabeçada",
            "S": "Soco",
        }

    def converter_escolha(self, escolha):
        return escolha.upper()

    def gerar_escolha_computador(self):
        return random.choice(list(self.OPCOES.keys()))

    def determinar_vencedor(self, jogador, computador):
        if jogador == computador:
            return " -0 Empate "
        elif jogador <= computador:
            return "Vitória pc"
        elif jogador >= computador:
            return "Vitória jogador"

    def jogar_partida(self):
        # Obtém a escolha do jogador
        escolha_jogador = self.converter_escolha(input("Digite sua escolha: Cabeçada ou Soco"))

        # Verifica se a escolha do jogador é válida
        while escolha_jogador not in self.OPCOES:
            escolha_jogador = self.converter_escolha(input("Escolha inválida. Digite sua escolha: Cabeçada ou Soco"))

        # Gera a escolha do computador
        escolha_computador = self.gerar_escolha_computador()

        # Determina o vencedor
        resultado = self.determinar_vencedor(escolha_jogador, escolha_computador)

        # Mostra os resultados da partida
        print(f"Você jogou {self.OPCOES[escolha_jogador]} e o computador jogou {self.OPCOES[escolha_computador]}.")
        print(f"{resultado}")

    def jogar_jogo(self):
        # Contador de partidas
        numero_partidas = 0

        # Contadores de vitórias, empates e derrotas
        vitorias = 0
        empates = 0
        derrotas = 0
        resultado = 0

        # Loop para jogar várias partidas
        while True:
            # Joga uma partida
            self.jogar_partida()

            # Incrementa o contador de partidas
            numero_partidas += 1

            # Pergunta se o jogador deseja continuar jogando
            continuar = input("Deseja continuar jogando (S/N)? ").upper()

            # Sai do loop se o jogador responder não
            if continuar == "N":
                break

            # Atualiza os contadores de acordo com o resultado da partida
            if resultado == "Vitória":
                vitorias += 1
            elif resultado == "Empate":
                empates += 1
            else:
                derrotas += 1

        # Mostra as estatísticas do jogo
        print(f"**Estatísticas do Jogo**")
        print(f"Número de partidas: {numero_partidas}")
        print(f"Vitórias: {vitorias}")
        print(f"Empates: {empates}")
        print(f"Derrotas: {derrotas}")

    # Inicia o jogo


jogo = rpg()
call_Jokenpo = jogo.jogar_jogo()

