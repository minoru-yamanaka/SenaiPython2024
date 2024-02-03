import datetime
TITULO = 'Descobrir ano futuro'
'''
Autor: Daniel
Data: 03/02/2024
Descrição:
Descobre em qual ano o usuário
terá 80 anos a partir da idade informada
'''
print('Bem vindo ao programa ' + TITULO)
print('Este programa descobre em que ano você terá x anos')
print('Você precisa informar sua idade atual')
print('A idade que gostaria de descobrir')

idade = int(input('Digite sua idade atual: '))
idade_futura = int(input('Digite qual idade você gostaria de descobrir: '))
ano_atual = datetime.datetime.now().year
falta_pro_futuro = idade_futura - idade
ano_futuro = ano_atual + falta_pro_futuro

print('Você terá ' + str(idade_futura) + ' anos em ' + str(ano_futuro))