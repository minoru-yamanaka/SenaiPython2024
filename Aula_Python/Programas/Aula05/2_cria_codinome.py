
# 2)	Crie uma função que um nome completo, a função irá criar
# um codinome que irá utilizar as 3 primeiras letras do primeiro
# nome e as 3 últimas letras do último nome.
# Ex: Daniel Santos   Dantos

def cria_codinome(nome_completo):
    partes_nome = nome_completo.split()
    primeiro_nome = partes_nome[0]
    ultimo_nome = partes_nome[-1]

    # Pegando as 3 primeiras letras do primeiro nome e as 3 últimas do último nome
    codinome = primeiro_nome[:3] + ultimo_nome[-3:]
    return codinome

# Exemplo de uso:
nome_completo = str(input("insira seu nome: "))
codinome = cria_codinome(nome_completo)
print(codinome)  # Saída: Dantos
