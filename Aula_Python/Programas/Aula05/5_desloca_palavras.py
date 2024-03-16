# 5)	Crie uma função que receba um texto e retorne o texto com as seguintes alterações:
# Faça o deslocamento de 3 letras para direita por palavra
#
# Exemplo: Usuário digitou “Aula de Python”
# Sistema retornou “ulaA ed honPyt”

def desloca_palavras(texto):
    texto_deslocado = ""
    for palavra in texto.split():
        palavra_deslocada = palavra[-3:] + palavra[:-3]
        texto_deslocado += palavra_deslocada + " "
    return texto_deslocado.strip()

# Exemplo de uso:
texto = str(input("insira seu texto: "))
texto_deslocado = desloca_palavras(texto)
print(texto_deslocado)  # Saída: ulaA ed honPyt

