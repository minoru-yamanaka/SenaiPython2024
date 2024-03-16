# 4)	Crie uma função que receba um texto e retorne o texto com as seguintes alterações:
# Retorne o texto com cada palavra invertida.
#
# Exemplo: Usuário digitou “Aula de Python”
# Sistema retornou “aluA ed nohtyP”
#

def inverte_palavras(frase):

    palavras = frase.split()

    palavras_invertidas = []  # Lista para armazenar as palavras invertidas

    for palavra in palavras:
        palavras_invertidas.append(palavra[::-1])

    frase_invertida = " ".join(palavras_invertidas)
    # inverte a palavra
    return frase_invertida[::-1]

frase = str(input("insira seu texto: "))

frase_invertida = inverte_palavras(frase)
print(frase_invertida)

# palavrai_invertida = palavra1[::-1]