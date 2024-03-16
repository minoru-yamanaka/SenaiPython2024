
def inversor_palavras(texto):
    palavras = texto.split(' ')
    texto_invertido = ''
    for palavra in palavras:
        texto_invertido += palavra[::-1] + ' '
    return texto_invertido[:-1]

print(inversor_palavras('Aula de Python'))
print(inversor_palavras(input('Digite um texto: ')))
