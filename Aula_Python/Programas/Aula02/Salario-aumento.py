
# 5)Uma empresa pretende fazer um reajuste salarial para os funcionários e precisa da sua ajuda para criar um programa.
# Ficou definido os seguintes reajustes:
# •	Salário Abaixo de R$1.500,00  Aumento de 25%
# •	Salário Entre de R$1.500,00 e R$1.999,99  Aumento de 20%
# •	Salário Entre de R$2.000,00 e R$2.999,99  Aumento de 15%
# •	Salário Entre de R$3.000,00 e R$4.999,99  Aumento de 10%
# •	Salário Igual ou Acima de R$5.000,00  Aumento de 5%

# Faça um programa que pergunte ao usuário qual seu Salário Atual e mostre ao usuário:
# 1.O salário atual;
# 2.A porcentagem do reajuste;
# 3.O aumento em R$;
# 4.O salário final após o reajuste.

class Salario:
    def __init__(self):
        salario = float(input('Insira seu salário: '))

        if salario < 1500:
            reajuste = salario * 0.25
            novo_salario = salario + reajuste
            print(f'Se seu salário é de ${salario}.\n Seu reajuste foi de 25%. \n O aumento foi de: ${reajuste} \n Ele foi reajustado para {novo_salario:.2f}.')

        elif salario <= 1500 or salario < 2000:
            reajuste = salario * 0.20
            novo_salario = salario + reajuste
            print(f'Se seu salário é de ${salario}.\n Seu reajuste foi de 20%. \n O aumento foi de: ${reajuste} \n Ele foi reajustado para {novo_salario:.2f}.')

        elif salario <= 2000 or salario < 3000:
            reajuste = salario * 0.15
            novo_salario = salario + reajuste
            print(f'Se seu salário é de ${salario}.\n Seu reajuste foi de 15%. \n O aumento foi de: ${reajuste} \n Ele foi reajustado para {novo_salario:.2f}.')

        elif salario <= 3000 or salario < 5000:
            reajuste = salario * 0.10
            novo_salario = salario + reajuste
            print(f'Se seu salário é de ${salario}.\n Seu reajuste foi de 10%. \n O aumento foi de: ${reajuste} \n Ele foi reajustado para {novo_salario:.2f}.')

        else:
            reajuste = salario * 0.05
            novo_salario = salario + reajuste
            print(f'Se seu salário é de ${salario}.\n Seu reajuste foi de 5%. \n O aumento foi de: ${reajuste} \n Ele foi reajustado para {novo_salario:.2f}.')

call_salario = Salario()
