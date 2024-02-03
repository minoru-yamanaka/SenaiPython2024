titulo = 'Calculadora de Fahrenheit'
'''
Data: 26/07/2023
Autor: Daniel
Descrição: Calcula a temperatura em Fahrenheit
a partir da temperatura em Celsius informada pelo usuário
'''
print('Bem vindo ao programa ' + titulo)

print('Por favor, informe a temperatura em ºC')
celsius = float(input())
fahrenheit = celsius * 1.8 + 32
print('A temperatura é ' + str(fahrenheit) + ' ºF')