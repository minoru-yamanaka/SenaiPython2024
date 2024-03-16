# 4)	Crie uma função que receba um texto e retorne o texto com as seguintes alterações:
# Retorne o texto com cada palavra invertida.
#
# Exemplo: Usuário digitou “Aula de Python”
# Sistema retornou “aluA ed nohtyP”
#

def inverte_palavras(texto):
    palavras = texto.split()
    palavras_invertidas = [palavra[::-1] for palavra in palavras]
    texto_invertido = ' '.join(palavras_invertidas)
    return texto_invertido

# Exemplo de uso:
texto = str(input("insira seu texto: "))
texto_invertido = inverte_palavras(texto)
print(texto_invertido)  # Saída: álO, odnum !nohtyP

def inversor_palavras(texto):
    palavras = texto.split(' ')
    texto_invertido = ''
    for palavra in palavras:
        texto_invertido += palavra[::-1] + ' '
    return texto_invertido[:-1]

print(inversor_palavras('Aula de Python'))
print(inversor_palavras(input('Digite um texto: ')))

