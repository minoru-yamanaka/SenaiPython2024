titulo = 'Caixa Eletrônico'
'''
Data: 31/07/2023
Autor: Daniel
Descrição: Verifica quais notas o usuario precisará
para sacar o dinheiro do valor informado
'''
print('Bem vindo ao programa ' + titulo)

valor_solicitado = int(input('Digite o valor a ser sacado: '))

notas_disponiveis_200 = 7
notas_disponiveis_100 = 7
notas_disponiveis_50 = 7
notas_disponiveis_20 = 7
notas_disponiveis_10 = 7
notas_disponiveis_5 = 7
notas_disponiveis_2 = 7
notas_disponiveis_1 = 7

valor_restante = valor_solicitado
if (valor_restante // 200) > notas_disponiveis_200:
    notas_200 = notas_disponiveis_200
else:
    notas_200 = valor_restante // 200
valor_restante -= notas_200 * 200

if (valor_restante // 100) > notas_disponiveis_100:
    notas_100 = notas_disponiveis_100
else:
    notas_100 = valor_restante // 100
valor_restante -= notas_100 * 100

if (valor_restante // 50) > notas_disponiveis_50:
    notas_50 = notas_disponiveis_50
else:
    notas_50 = valor_restante // 50
valor_restante -= notas_50 * 50

if (valor_restante // 20) > notas_disponiveis_20:
    notas_20 = notas_disponiveis_20
else:
    notas_20 = valor_restante // 20
valor_restante -= notas_20 * 20

if (valor_restante // 10) > notas_disponiveis_10:
    notas_10 = notas_disponiveis_10
else:
    notas_10 = valor_restante // 10
valor_restante -= notas_10 * 10

if (valor_restante // 5) > notas_disponiveis_5:
    notas_5 = notas_disponiveis_5
else:
    notas_5 = valor_restante // 5
valor_restante -= notas_5 * 5

if (valor_restante // 2) > notas_disponiveis_2:
    notas_2 = notas_disponiveis_2
else:
    notas_2 = valor_restante // 2
valor_restante -= notas_2 * 2

if (valor_restante // 1) > notas_disponiveis_1:
    notas_1 = notas_disponiveis_1
else:
    notas_1 = valor_restante // 1
valor_restante -= notas_1 * 1

print('Valor solicitado: ' + str(valor_solicitado))
if notas_200 > 0:
    print('Notas de R$200,00 : ' + str(notas_200))
if notas_100 > 0:
    print('Notas de R$100,00 : ' + str(notas_100))
if notas_50 > 0:
    print('Notas de R$50,00 : ' + str(notas_50))
if notas_20 > 0:
    print('Notas de R$20,00 : ' + str(notas_20))
if notas_10 > 0:
    print('Notas de R$10,00 : ' + str(notas_10))
if notas_5 > 0:
    print('Notas de R$5,00 : ' + str(notas_5))
if notas_2 > 0:
    print('Notas de R$2,00 : ' + str(notas_2))
if notas_1 > 0:
    print('Notas de R$1,00 : ' + str(notas_1))

if valor_restante > 0:
    print('Valor que não foi possível sacar: ' + str(valor_restante))