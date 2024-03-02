def adicao(a, b):
    if b == 0:
        return a
    else:
        return adicao(a + 1, b - 1)


def subtracao(a, b):
    if b == 0:
        return a
    else:
        return subtracao(a - 1, b - 1)


def multiplicacao(a, b):
    if b == 0:
        return 0
    elif b == 1:
        return a
    else:
        return adicao(a, multiplicacao(a, b - 1))


def divisao(a, b):
    if a < b:
        return 0
    else:
        return adicao(1, divisao(subtracao(a, b), b))


# Função principal para testar as operações
def main():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    print("Adição:", adicao(num1, num2))
    print("Subtração:", subtracao(num1, num2))
    print("Multiplicação:", multiplicacao(num1, num2))
    print("Divisão:", divisao(num1, num2))



main()
