def deslocar_palavras(texto, deslocamento):
    palavras = texto.split()  # Divide o texto em palavras

    texto_deslocado = ''  # Variável para armazenar o texto deslocado

    for palavra in palavras:
        # Verifica se a palavra tem mais de duas letras para realizar o deslocamento
        if len(palavra) > 2:
            texto_deslocado += palavra[deslocamento:] + palavra[:deslocamento] + ' '
        else:
            # Se a palavra tiver duas letras ou menos, inverte a ordem das letras
            texto_deslocado += palavra[::-1] + ' '

    # Retorna o texto deslocado
    return texto_deslocado.strip()  # Remove o espaço em branco extra no final

# Solicita ao usuário que insira um texto
texto = input('Digite um texto: ')

# Solicita ao usuário que insira o deslocamento
deslocamento = int(input('Insira o deslocamento: '))

# Chama a função deslocar_palavras com o texto e o deslocamento fornecidos
texto_deslocado = deslocar_palavras(texto, deslocamento)

# Imprime o texto deslocado
print(texto_deslocado)
