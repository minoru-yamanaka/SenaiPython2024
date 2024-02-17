import datetime


# 12) Faça um programa que realize o cadastro de um usuário a partir de seu nome, idade, peso, altura que deverão ser informados pelo usuário e exiba a frase: Seu nome é ______ e tem ___ caracteres, você tem ___ anos e nasceu no ano de ______. Você mede _____cm, pesa ____ Kg e seu IMC é:____. Não esqueça de manter uma boa interface com o usuário!!
# # *Fórmula do cálculo do IMC: IMC = Peso ÷ (Altura × Altura)
# Peso em KG
# Altura em metros
class IMC:
    def __init__(self):
        print('Ficha de Cadastro')
        print('Nome: ')
        nome = input()
        print('Idade: ')
        idade = int(input())

        data = datetime.datetime.now().year

        anoNascimento = idade - int(data)
        anoNascimento = anoNascimento * -1
        print('Peso:')
        peso = float(input())
        print('Altura: ')
        altura = float(input())
        imc = peso / (altura ** 2)
        print('Seu nome é ' + nome + '\n e tem ' + str(len(nome)) + ' caracteres, \n você tem ' + str(
            idade) + ' anos e nasceu no ano de ' + str(anoNascimento) + '\n Você mede ' + str(
            altura) + ' cm, pesa ' + str(peso) + ' Kg e \n seu IMC é ' + f"{imc:.2f}" + '.')


call_IMC = IMC()
