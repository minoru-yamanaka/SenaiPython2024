# 4)Uma ótica quer fazer um desconto diferenciado com base na idade do usuário em um modelo de óculos que custa R$200,00.
# O desconto será igual a idade do usuário, porém o desconto mínimo será 10% e o desconto máximo será de 80%.
# Faça um programa que pergunte a idade do usuário e então mostre o valor final do óculos e o desconto adquirido.

class OticaDesconto:
    def __init__(self):

        oculos = float(input('Insira o valor do Óculos: '))
        idade = int(input('Insira sua idade: '))
        idade = float(idade)
        desconto = (oculos * idade)//100

        print(desconto)

        if desconto < 10:
            desconto = (oculos * 10) // 100
            valor = oculos - desconto
            print('O desconto adquirido é de: ' + str(desconto) + ' e o valor do óculos é: $ '+ str(valor))
        elif desconto > 80:
            desconto = (oculos * 80) // 100
            valor = oculos - desconto
            print('O desconto adquirido é de: ' + str(desconto) + ' e o valor do óculos é: $ ' + str(valor))
        else:
            valor = oculos - desconto
            print('O valor do óculos é: $' + str(valor))
call_OticaDesconto = OticaDesconto()