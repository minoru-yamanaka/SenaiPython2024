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
jogo.run()  # Chamar o método run() para executar o jogo