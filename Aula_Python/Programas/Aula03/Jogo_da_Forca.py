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