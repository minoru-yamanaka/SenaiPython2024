titulo = 'Calculadora de Dolares'
'''
Data: 26/07/2023
Autor: Daniel
Descrição: Calcula quantos dolares o usuario
teria quando convertido do valor em real
'''
print('Bem vindo ao programa ' + titulo)

print('Quantos reais você quer converter?')
reais = float(input())
print('Quanto está o valor do dolar hoje?')
cota_us = float(input())

dolares = reais / cota_us

#print('Este valor equivale a ' + str(dolares) + ' dolares')
print('Este valor equivale a {:.2f} dolares'.format(dolares))
