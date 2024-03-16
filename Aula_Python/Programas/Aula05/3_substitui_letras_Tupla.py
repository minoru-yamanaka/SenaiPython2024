# 3)	Crie uma função que receba um texto e retorne o texto com as seguintes alterações:
# Letra A  4
# Letra B  8
# Letra E  3
# Letra I  1
# Letra O  0
# Letra T  7

def substitui_letras(texto):
    # Dicionário contendo as substituições de letras por números
    Tradutor = {'A': '4', 'B': '8', 'E': '3', 'I': '1', 'O': '0', 'T': '7'}

    # Loop que percorre todas as chaves e
    # valores do dicionário substituicoes
    for key, valor in Tradutor.items():
        # Substitui todas as ocorrências da
        # letra atual no texto pela sua substituição correspondente
        texto = texto.replace(key, valor)

    # Retorna o texto modificado
    return texto


# Exemplo de uso:
# Solicita ao usuário que insira um nome e converte para letras maiúsculas
texto = str(input("insira seu nome: ").upper())

# Chama a função substitui_letras passando o texto inserido como argumento
texto_modificado = substitui_letras(texto)

# Imprime o texto modificado
print(texto_modificado)  # Saída: 4ul4 d3 Py7h0n
