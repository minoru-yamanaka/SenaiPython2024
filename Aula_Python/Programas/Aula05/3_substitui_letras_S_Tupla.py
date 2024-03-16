def substitui_letras(texto):
    # Dicionário contendo as substituições de letras por números
    substituicoes = {'A': '4', 'B': '8', 'E': '3', 'I': '1', 'O': '0', 'T': '7'}

    # Loop que percorre todas as chaves do dicionário substituicoes
    for letra in substituicoes:
        # Verifica se a letra está presente no texto
        if letra in texto:
            # Substitui todas as ocorrências da letra atual no texto pela sua substituição correspondente
            texto = texto.replace(letra, substituicoes[letra])

    # Retorna o texto modificado
    return texto


# Exemplo de uso:
# Solicita ao usuário que insira um texto e converte para letras maiúsculas
texto = str(input("Insira seu texto: ").upper())

# Chama a função substitui_letras passando o texto inserido como argumento
texto_modificado = substitui_letras(texto)

# Imprime o texto modificado
print(texto_modificado)
