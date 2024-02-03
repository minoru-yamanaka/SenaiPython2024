import datetime

#  ctrl + / = comenta.

# 1) Quais destes são operadores e quais são valores:
# *	operadores
# ‘ola’	valores
# -15.3	valores
# -	operadores
# /	operadores
# +	operadores
# 22	valores

# 2) Quais destes nomes podem ser utilizados para criação de variáveis:
# ‘teste’	x
# Teste	v
# _teste	v
# 42_teste	x
# joaoCardoso	v
# 1Caixa	x
# ‘nomeCompleto’	x
# botao4LigaLampada	v

# 3) Indique qual o tipo de cada variável abaixo:
# “a”	str
# 12	int
# Senai	Não válido
# 1.5	float
# True	Bolean
# ‘55’	str
# ‘False’	str
# “Verdadeiro ou Falso?”	str

# 4)	Qual o resultado do código a seguir:
# alunos = 15
# alunos = alunos + 1
# print(alunos)
# 16

# 5)	Qual o resultado do código a seguir:
# alunos = ‘15’
# alunos = alunos + ‘1’
# print(alunos)
# 151


class vendedor:
    def __init__(self):
        vendedor = 'Minoru'
        vendas = 400
        meta = 500

        if vendas >= meta:
            print(str(vendedor) + " Bateu a meta")
        else:
            print(str(vendedor) + " Não bateu a meta")
# call_vendedor = vendedor()

# 6) Monte um programa que exiba a soma de dois números inteiros.
class soma:
    def __init__(self):
        # Somando números:
        n1 = 3
        n2 = 4
        resultado = n1 + n2
        print('A soma dos números é: ' + str(resultado))
# call_soma = soma()

# 7) Monte um programa que exiba a soma de dois números inteiros informados pelo usuário.
# Somando números:

class somaInput:
    def __init__(self):
        print('Insira o 1° número: ')
        n1 = input()
        int(n1)
        print('Insira o 2° número: ')
        n2 = input()
        r = int(n1) + int(n2)
        print(r)
# call_somaInput = somaInput()

# 8) Faça um programa que mostre em que ano a pessoa terá 80 anos a partir da idade informada pelo usuário. Não esqueça de manter uma boa interface com o usuário!

class exibirAniversario:
    def __init__(self):
        print('Insira o seu ano de nascimento: ')
        nascimento = input()
        idade = int(nascimento) - 2024
        idade = idade * -1
        print('Você tem: ' + str(idade) + ' anos')
# call_exibir_aniversario = exibirAniversario()

# 9) Um professor gostaria um programa para auxiliá-lo a montar a média final de seus alunos. Sabendo que são 2 notas por semestre, monte um programa que através das notas informadas pelo usuário mostre a sua média final. Não esqueça de manter uma boa interface com o usuário!!
class mediaFinal:
    def __init__(self):
            print('Insira a 1° nota do semestre: ')
            n1 = input()
            int(n1)
            print('Insira a 2° nota do semestre: ')
            n2 = input()
            r = int(n1) + int(n2)
            mediaFinal = r // 2
            print('A média final é: ' + str(mediaFinal) )
# call_mediaFinal = mediaFinal()

# 10) Faça um programa para converter Reais em Dólares informado pelo usuário:
# Escala: R$5,00      U$1,00

class conveterMoedas:
    def __init__(self):
        print('Insira a valor em Reais a converter: ')
        reais = float(input())
        print('Insira a valor do Dólar: ')
        dolares = float(input())
        convercao = reais / dolares
        print('O valor de R$ ' + str(reais) + ' reais' + ' = USD ' + str(convercao) + ' dólares')
# call_conveterMoedas = conveterMoedas()

# 11) Faça um programa para converter Graus Celsius em Fahrenheit informado pelo usuário:
# Escala: 0 ~ 100 ºC         32 ~ 212 ºF
# converter graus Celsius em graus Fahrenheit multiplique por 1,8 e adicione 32
class graus:
    def __init__(self):
        print('Insira a valor em Graus Celsius a converter: ')
        Celsius = float(input())
        Fahrenheit = Celsius * 1.8 + 32
        print(str(Celsius) + 'ºC  ' + str(Fahrenheit) + 'ºF')
# call_graus = graus()

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
        print('Seu nome é ' + nome + '\n e tem ' + str(len(nome)) + ' caracteres, \n você tem ' + str(idade) + ' anos e nasceu no ano de ' + str(anoNascimento) + '\n Você mede ' + str(altura) + ' cm, pesa ' + str(peso) + ' Kg e \n seu IMC é ' + f"{imc:.2f}" + '.' )
# call_IMC = IMC()

# 13) Um fabricante de tintas quer montar um programa que auxilie o comprador a saber quantas latas de tinta ele precisará para pintar sua parede.
# Monte um programa em python que execute esta função a partir dos dados informados pelo usuário (largura e altura),
# sabendo que cada lata de tinta cobre 3m² de parede. Não esqueça de manter uma boa interface com o usuário!!

class tintas:
    def __init__(self):
        print("Bem-vindo ao Calculador de Latas de Tinta!")
        largura = float(input("Informe a largura da parede em metros: "))
        altura = float(input("Informe a altura da parede em metros: "))

        # em metros quadrados
        coberturaPorLata = 3
        # Calcula a área da parede
        areaParede = largura * altura
        # Calcula a quantidade de latas necessárias (arredondando para cima)
        latasNecessarias = -(-areaParede // coberturaPorLata)

        # Exibindo o resultado
        print('Para pintar uma parede de ' + str(largura) + ' m x ' + str(largura) + ' m, você precisará de ' +  str(latasNecessarias) + ' latas de tinta.')
# call_tintas = tintas()

class tintas2:
    def __init__(self):
        print("Bem-vindo ao Calculador de Latas de Tinta!")
        largura = float(input("Informe a largura da parede em metros: "))
        altura = float(input("Informe a altura da parede em metros: "))

        # Calcula a área da parede
        areaParede = largura * altura

        latas_inteiro = areaParede // 3
        latas_resto = areaParede% 3 > 0
        latas_total = latas_inteiro + latas_resto

        # Exibindo o resultado
        print('Para pintar uma parede de ' + str(largura) + ' m x ' + str(largura) + ' m, você precisará de ' +  str(latas_total) + ' latas de tinta.')
# call_tintas2 = tintas2()