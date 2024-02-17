# 1)	Faça um programa para adivinhar um número de 1 a 10000.
# Se você errar o computador deverá responder se é mais ou menos.
# Se você errar 10 vezes você perde o jogo

import random
from idlelib import run


class adivinharNumero:
    def __init__(self):

        tent = 0
        numeroGerado = random.randint(1, 10000)

        while tent < 10:
            print('Tentativa:  ' + str(tent))
            chuteUsuario = int(input('Tente adivinhar o número escolhido pelo pc: '))

            if chuteUsuario == numeroGerado:
                print('Parabéns! Você adivinhou o número. O número é: ' + str(numeroGerado))
                break
            elif chuteUsuario < numeroGerado:
                tent += 1
                print('O número é maior.')
            else:
                tent += 1
                print('O número é menor.')
        else:
            print('Você errou o máximo de vezes. O número é: ' + str(numeroGerado))
# call_adivinharNumero = adivinharNumero()


# 2) Faça um programa para avaliar qual o número que mais
# cai em um lance de dois dados (D6).
# O sistema deverá lançar um conjunto de dois
# dados n vezes seguidas, onde n é o número de
# vezes que você informar ao computador.
# Após jogar os dados, o sistema deverá informar quantas vezes
# a soma deu cada um dos números
# possíveis: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 e 12.

class lance:
    def __init__(self):
        # biblioteca random para gerar números aleatórios

        # Define o número de lançamentos
        lancamentos = int(input("Digite o número de lançamentos: "))

        # Cria um dicionário para armazenar as ocorrências
        ocorrencias = {}
        for soma in range(2, 13):
            ocorrencias[soma] = 0

        # Simula o lançamento dos dados n vezes
        for _ in range(lancamentos):
            # Obtém a soma dos dados
            dado1 = random.randint(1, 6)
            dado2 = random.randint(1, 6)
            soma = dado1 + dado2
            # Incrementa a contagem da soma no dicionário
            ocorrencias[soma] += 1

        # Mostra os resultados
        for soma, contagem in ocorrencias.items():
            print(f"Soma {soma}: {contagem} ocorrências")

        # Mostra o número que mais cai
        maior_contagem = max(ocorrencias.values())
        soma_mais_frequente = [soma for soma, contagem in ocorrencias.items() if contagem == maior_contagem]
        print(f"A soma que mais cai é {soma_mais_frequente} ({maior_contagem} ocorrências)")

# call_lance = lance()

# 3) Faça um jogo de Pedra, Papel e Tesoura.
# No qual você digitará a letra P para jogar Papel, a letra R para jogar Pedra e a letra T para jogar Tesoura.
# Você jogará contra o computador e contabilizara o número de vitórias, empates e derrotas
import random
class Jokenpo1:
    def __init__(self):
        self.rodadas = 0
        self.restart = 0
        self.escolhaComputador = 0
        self.placarJogador = 0
        self.placarComputador = 0

    def exibeResultado(self):
        if self.placarJogador > self.placarComputador:
            print("!!! JOGADOR GANHOU !!!")
        elif self.placarComputador > self.placarJogador:
            print("!!! COMPUTADOR GANHOU !!!")
        else:
            print("::: EMPATE :::")

    def verificaResultado(self):
        if (self.escolhaJogador == 1 and self.escolhaComputador == 2) or \
                (self.escolhaJogador == 2 and self.escolhaComputador == 3) or \
                (self.escolhaJogador == 3 and self.escolhaComputador == 1):
            self.placarComputador += 1
        elif (self.escolhaJogador == 1 and self.escolhaComputador == 3) or \
                (self.escolhaJogador == 2 and self.escolhaComputador == 1) or \
                (self.escolhaJogador == 3 and self.escolhaComputador == 2):
            self.placarJogador += 1
        elif self.escolhaJogador == self.escolhaComputador:
            print("O COMPUTADOR ESCOLHEU O MESMO QUE VOCÊ, REPITA:")
        else:
            print("!!! NÚMERO INVÁLIDO !!!")

    def exibePlacar(self):
        print("::: PLACAR :::")
        print("Jogador:", self.placarJogador)
        print("Computador:", self.placarComputador)

    def rotuloEscolhaJogador(self):
        print("::: JOGADOR, DIGITE:")
        print("::: [1] Pedra   :::")
        print("::: [2] Papel   :::")
        print("::: [3] Tesoura :::")
        print("-------------------")
        print("Escolha sua opção: ")

    def run(self):
        while self.restart == 0:
            self.rodadas = int(input("::: JOKENPÔ :::\nINSIRA A QUANTIDADE DE RODADAS: "))
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

jogo = Jokenpo1()  # Criar um objeto da classe Jokenpo1
# jogo.run()  # Chamar o método run() para executar o jogo


# 3) Faça um jogo de Pedra, Papel e Tesoura.
# No qual você digitará a letra P para jogar Papel, a letra R para jogar Pedra e a letra T para jogar Tesoura.
# Você jogará contra o computador e contabilizara o número de vitórias, empates e derrotas

class Jokenpo:
    def __init__(self):
        self.OPCOES = {
            "P": "Papel",
            "R": "Pedra",
            "T": "Tesoura",
        }

    def converter_escolha(self, escolha):
        return escolha.upper()

    def gerar_escolha_computador(self):
        return random.choice(list(self.OPCOES.keys()))

    def determinar_vencedor(self, jogador, computador):
        if jogador == computador:
            return "Empate"
        elif jogador == "P" and computador == "T":
            return "Vitória"
        elif jogador == "P" and computador == "R":
            return "Derrota"
        elif jogador == "R" and computador == "P":
            return "Vitória"
        elif jogador == "R" and computador == "T":
            return "Derrota"
        elif jogador == "T" and computador == "P":
            return "Derrota"
        elif jogador == "T" and computador == "R":
            return "Vitória"

    def jogar_partida(self):
        # Obtém a escolha do jogador
        escolha_jogador = self.converter_escolha(input("Digite sua escolha (P/R/T): "))

        # Verifica se a escolha do jogador é válida
        while escolha_jogador not in self.OPCOES:
            escolha_jogador = self.converter_escolha(input("Escolha inválida. Digite sua escolha (P/R/T): "))

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
jogo = Jokenpo()
# call_Jokenpo = jogo.jogar_jogo()



# 4)    Faça um jogo de batalha entre você e o computador:
#    - Cada um dos jogadores inicia com 10 pontos de vida.
#    - Neste jogo, você deverá comparar o poder de combate em cada turno;
#    quem ganhar desfere o ataque no oponente causando o dano respectivo.
#    - Você tem dois ataques, que poderá selecionar no início de cada rodada:
#      1. **Cabeçada**: Tem poder de combate 4, se ganhar tira 3 de vida do oponente e toma 1 de dano.
#      2. **Soco**: Tem poder de combate aleatório (jogar no dado D6) e, caso ganhe, causa dano aleatório (jogar no dado D6).
#    - O computador tem apenas o ataque Soco.
#    - Quem chegar a 0 pontos de vida perde o jogo.




# 5)	Faça um jogo da forca com 10 tentativas

class JogoDaForca:

    def __init__(self):
        self.palavras = ["banana", "maçã", "laranja", "abacaxi", "morango", "uva", "kiwi", "pêssego", "melancia", "mamão"]
        self.tentativas_restantes = 10

    def gerar_palavra_aleatoria(self):
        return random.choice(self.palavras)

    def converter_palavra_para_lista(self, palavra):
        return list(palavra)

    def inicializar_letras_acertadas(self, palavra):
        letras_acertadas = []
        for _ in range(len(palavra)):
            letras_acertadas.append("_")
        return letras_acertadas

    def mostrar_jogo(self, letras_acertadas, tentativas_restantes):
        print(f"Letras acertadas: {' '.join(letras_acertadas)}")
        print(f"Tentativas restantes: {tentativas_restantes}")

    def obter_palavra_do_jogador(self):
        return input("Digite uma letra: ").upper()

    def verificar_palavra(self, palavra):
        return palavra == self.palavra_secreta

    def jogar_partida(self):
        self.palavra_secreta = self.gerar_palavra_aleatoria()
        letras_acertadas = self.inicializar_letras_acertadas(self.palavra_secreta)

        while self.tentativas_restantes > 0 and not self.verificar_palavra("".join(letras_acertadas)):
            self.mostrar_jogo(letras_acertadas, self.tentativas_restantes)
            letra_jogador = self.obter_palavra_do_jogador()

            if letra_jogador in self.palavra_secreta:
                for i, letra in enumerate(self.palavra_secreta):
                    if letra == letra_jogador:
                        letras_acertadas[i] = letra
            else:
                self.tentativas_restantes -= 1

        self.mostrar_jogo(letras_acertadas, self.tentativas_restantes)
        if self.verificar_palavra("".join(letras_acertadas)):
            print("Você venceu!")
        else:
            print(f"Você perdeu! A palavra era: {self.palavra_secreta}")

# Inicia o jogo
#jogo = JogoDaForca()
#jogo.jogar_partida()





