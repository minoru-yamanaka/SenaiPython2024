TITULO = 'Descobrir ano futuro'
'''
Autor: Profº Daniel
Data: 03/02/2024
Descrição:
Descobre em qual ano o usuário
terá 80 anos a partir da idade informada
'''
print('Bem vindo ao programa ' + TITULO)

idade = int(input('Digite sua idade: '))
falta_pra_80 = 80 - idade
idade_futura = 2024 + falta_pra_80

print('Você terá 80 anos em ' + str(idade_futura))