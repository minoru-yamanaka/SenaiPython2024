# Definição da classe Estrutura
class Estrutura:
    # Método para completar um nome com 'mon'
    def completa_com_mon(self, nome):
        # Verifica se o comprimento do nome é maior ou igual a 4 caracteres
        if len(nome) >= 4:
            # Se for, pega os primeiros 4 caracteres do nome
            prefixo = nome[:4]
            # Concatena 'mon' ao prefixo e retorna o nome completo
            return prefixo + 'mon'
        else:
            # Se o nome for muito curto, retorna uma mensagem indicando isso
            return "O nome é muito curto para ser completado com 'mon'."

# Criar uma instância da classe Estrutura
estrutura = Estrutura()

# Exemplo de uso:
# Solicita ao usuário que insira seu nome
nome = input("Insira seu nome: ")
# Chama o método completa_com_mon da instância estrutura, passando o nome inserido como argumento
nome_completo = estrutura.completa_com_mon(nome)
# Imprime o nome completo
print(nome_completo)  # Saída: Danimon
