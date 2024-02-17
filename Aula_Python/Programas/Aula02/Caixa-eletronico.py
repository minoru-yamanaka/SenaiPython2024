
# 8)Faça um programa de um caixa eletrônico que, a partir do valor a ser sacado informado pelo usuário, o programa informe a menor quantidade de cédulas que o usuário irá receber, informando-o quantas cédulas e de quais valores ele irá receber.
# Considerar apenas notas:
# R$200,00
# R$100,00
# R$50,00
# R$20,00
# R$10,00
# R$5,00
# R$2,00
# R$1,00
# Exemplo:
# R$ 858,00
# O programa irá informar:
# Cédulas de 200 reais: 4
# Cédulas de 50 reais: 1
# Cédulas de 5 reais: 1
# Cédulas de 2 reais: 1
# Cédulas de 1 real: 1

class Caixa:
    def __init__(self):
        # Solicita ao usuário que informe o valor a ser sacado

        valor_sacado = int(input("Informe o valor a ser sacado: R$"))

#       Solicita ao usuário que informe o valor a ser sacado e converte
#       a entrada para um número inteiro

        valor_sacado = int(input("Informe o valor a ser sacado: R$"))

        # Inicializa as variáveis para contar a quantidade de cada cédula
        cedula_200 = 0
        cedula_100 = 0
        cedula_50 = 0
        cedula_20 = 0
        cedula_10 = 0
        cedula_5 = 0
        cedula_2 = 0
        cedula_1 = 0

        # Calcula a quantidade de cada cédula necessária para compor o valor informado,
        # utilizando a divisão '//' e o operador de módulo'%':
        cedula_200 = valor_sacado // 200
        valor_sacado %= 200

        cedula_100 = valor_sacado // 100
        valor_sacado %= 100

        cedula_50 = valor_sacado // 50
        valor_sacado %= 50

        cedula_20 = valor_sacado // 20
        valor_sacado %= 20

        cedula_10 = valor_sacado // 10
        valor_sacado %= 10

        cedula_5 = valor_sacado // 5
        valor_sacado %= 5

        cedula_2 = valor_sacado // 2
        valor_sacado %= 2

        cedula_1 = valor_sacado // 1

        # Exibe a quantidade de cada cédula, se a quantidade for maior que zero:
        if cedula_200 > 0:
            print(f"Cédulas de 200 reais: {cedula_200}")
        if cedula_100 > 0:
            print(f"Cédulas de 100 reais: {cedula_100}")
        if cedula_50 > 0:
            print(f"Cédulas de 50 reais: {cedula_50}")
        if cedula_20 > 0:
            print(f"Cédulas de 20 reais: {cedula_20}")
        if cedula_10 > 0:
            print(f"Cédulas de 10 reais: {cedula_10}")
        if cedula_5 > 0:
            print(f"Cédulas de 5 reais: {cedula_5}")
        if cedula_2 > 0:
            print(f"Cédulas de 2 reais: {cedula_2}")

class_Caixa = Caixa()