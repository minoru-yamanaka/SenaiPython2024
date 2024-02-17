# Exemplos:

class Estrutura:
    def __init__(self):
        print('Qual o seu nome?')
        nome = input().lower()

        if nome == "daniel":
            print('Olá Daniel')
            print('Sua senha é 40028922')
        elif nome == 'jorge':
            print('Olá, seja bem-vindo')
            print('Sua senha é 20268406')
        else:
            print("Você não é nem Daniel nem Jorge")
# call_Estrtutura = Estrutura()


class idade:
    def __init__(self):
        print('Qual sua idade?')
        idade = int(input())

        if idade < 12:
            print('Você é menor de idade')
        elif idade > 200:
            print('Você é maior de idade (possivelmente muito maior!)')
        else:
            print('Você não é nem Daniel nem Jorge')

# call_idade = idade()

# Atividades | Exercícios

# 1)Faça um programa que peça um número ao usuário e informe se é Par ou Ímpar.
class ParouImpar:
    def __init__(self):
        num = float(input('Insira um número: '))
        resultado = num % 2

        if resultado == 0:
            print('Este número é Par ')
        else :
            print('Este número é Ímpar ')

# call_ParouImpar = ParouImpar()

# 2)Uma empresa de transporte público quer fazer um sistema automático para identificar se o usuário terá gratuidade
# no transporte ou não. Faça um programa que pergunte a idade do usuário, se ele tiver 65 anos ou mais irá informar que
# ele tem gratuidade no transporte.

class GratuidadeNoTransporte:
    def __init__(self):
        idade = int(input('Insira sua idade: '))

        if idade >= 65:
            print('Este o usuário tem gratuidade no transporte')
        else :
            print('Este o usuário não tem gratuidade no transporte')

# call_GratuidadeNoTransporte = GratuidadeNoTransporte()

# 3)Faça um programa que pede duas notas de um aluno.
# Em seguida ele deve calcular a média do aluno e dar o seguinte resultado:
# •	Aprovado  Acima de 7
# •	Reprovado  Abaixo de 5
# •	Recuperação  Entre 5 e 7

class NotasAluno:
    def __init__(self):
        print('Insira a 1° nota do semestre: ')
        n1 = input()
        int(n1)
        print('Insira a 2° nota do semestre: ')
        n2 = input()
        r = int(n1) + int(n2)
        mediaFinal = r // 2

        if mediaFinal < 5:
            print('Este o aluno está Reprovado')
        elif mediaFinal > 7:
            print('Este o aluno está Aprovado')
        else:
            print('Este o aluno está de Recuperação')

# call_NotasAluno = NotasAluno()

# 4)Uma ótica quer fazer um desconto diferenciado com base na idade do usuário em um modelo de óculos que custa R$200,00.
# O desconto será igual a idade do usuário, porém o desconto mínimo será 10% e o desconto máximo será de 80%.
# Faça um programa que pergunte a idade do usuário e então mostre o valor final do óculos e o desconto adquirido.

class OticaDesconto:
    def __init__(self):

        # Se houver uma constante ela devera se maiuscula e snake = MAIUSCULA_CONSTANTE

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
# call_OticaDesconto = OticaDesconto()


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

# call_salario = Salario()

# EXERCÍCIOS EXTRA

# 6)Leia o texto abaixo sobre o Ano Bissexto:
# “O calendário gregoriano, estabelecido pela primeira vez em 1582 pelo Papa Gregório XIII, foi projetado para corrigir
# os erros introduzidos pelo calendário juliano, que é menos preciso.
# No calendário gregoriano, um ano normal consiste em 365 dias. Como o comprimento real de um ano sideral
# (o tempo necessário para a Terra girar uma vez sobre o Sol) é na verdade de 365,2425 dias, um "ano bissexto"# de 366
# dias é usado uma vez a cada quatro anos para eliminar o erro causado por três anos normais (mas curtos).
# Qualquer ano que seja uniformemente divisível por 4 é um ano bissexto: por exemplo, 1988, 1992 e 1996 são anos bissextos.
# No entanto, ainda há um pequeno erro que deve ser contabilizado. Para eliminar esse erro, o calendário gregoriano
# estipula que um ano que é uniformemente divisível por 100 (por exemplo, 1900) é um ano bissexto apenas se também
# é igualmente divisível por 400.
# Por essa razão, os seguintes anos não são bissextos:
# 1700, 1800, 1900, 2100, 2200, 2300, 2500, 2600:
# Isso porque eles são uniformemente divisíveis por 100, mas não por 400.
# Os seguintes anos são bissextos: 1600, 2000, 2400
# Isso porque eles são uniformemente divisíveis por 100 e 400.”
# Faça um programa no qual o usuário informe um ano e o sistema responda se o ano é bissexto ou não.

class AnoBissexto:
    def __init__(self):
        # Solicita ao usuário que informe um ano e converte a entrada para inteiro
        ano_informado = int(input("Informe o ano: "))

        # Verifica se o ano é bissexto e imprime a mensagem correspondente
        if ano_informado % 4 == 0 and (ano_informado % 100 != 0 or ano_informado % 400 == 0):

        # - ano_informado % 4 == 0: Isso verifica se o ano é divisível  por 4, pois os anos bissextos
        # geralmente têm essa  propriedade.
        # - ano_informado % 100 != 0: Este é um segundo critério para garantir que o ano não seja divisível
        # por 100, a menos que:
        # - ano_informado % 400 == 0: Se  o  ano for divisível por 100,
        # ele ainda pode ser bissexto se for divisível por 400.

            print(f"O ano {ano_informado} é bissexto.")
        else:
            print(f"O ano {ano_informado} não é bissexto.")
# call_AnoBissexto = AnoBissexto()

# 7)Faça um programa que pergunte uma data ao usuário (dia, mês e ano separadamente) e valide se aquela data é real ou não, fazendo as seguintes validações:
# •	Verificar se o dia informado existe dentro daquele mês
# o	Tem 31 dias se o mês for 1, 3, 5, 7, 8, 10 ou 12;
# o	Tem 30 dias se o mês for 4, 6, 9 ou 11;
# o	Tem 28 dias se o mês for 2 e o ano não for bissexto;
# o	Tem 29 dias se o mês for 2 e o ano for bissexto.
# •	Verificar se o mês informado existe (ano vai até 12 meses);
# •	Verificar se o dia, mês e ano são valores positivos.
# Informar ao usuário se a data for válida ou não.

class DataReal:
    def __init__(self):
        # Solicita ao usuário que informe o dia, mês e ano separadamente
        dia = int(input("Informe o dia: "))
        mes = int(input("Informe o mês: "))
        ano = int(input("Informe o ano: "))

        # Verifica se o ano é bissexto
        ano_bissexto = ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

        # Verifica se o mês e o dia estão dentro dos limites
        if 1 <= mes <= 12 and 1 <= dia <= 31 and mes == 1 or \
                1 <= mes <= 12 and 1 <= dia <= 31 and mes == 3 or \
                1 <= mes <= 12 and 1 <= dia <= 31 and mes == 5 or \
                1 <= mes <= 12 and 1 <= dia <= 31 and mes == 7 or \
                1 <= mes <= 12 and 1 <= dia <= 31 and mes == 8 or \
                1 <= mes <= 12 and 1 <= dia <= 31 and mes == 10 or \
                1 <= mes <= 12 and 1 <= dia <= 31 and mes == 12 or \
                1 <= mes <= 12 and 1 <= dia <= 30 and mes == 4 or \
                1 <= mes <= 12 and 1 <= dia <= 30 and mes == 6 or \
                1 <= mes <= 12 and 1 <= dia <= 30 and mes == 9 or \
                1 <= mes <= 12 and 1 <= dia <= 30 and mes == 11 or \
                (ano_bissexto and 1 <= dia <= 29 and mes == 2) or \
                (not ano_bissexto and 1 <= dia <= 28 and mes == 2):
            print("Data válida!")
        else:
            print("Data inválida!")
# class_DataReal = DataReal()

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

       # Solicita ao usuário que informe o valor a ser sacado e converte
       # a entrada para um número inteiro

        valor_sacado = float(input("Informe o valor a ser sacado: R$"))

        # Calcula a quantidade de cada cédula necessária para compor o valor informado,
        # utilizando a divisão '//' e o operador de módulo'%':

        cedula_200 = valor_sacado // 200
        valor_sacado = valor_sacado % 200

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



